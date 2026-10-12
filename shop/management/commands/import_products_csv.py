import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from shop.models import Product


class Command(BaseCommand):
    help = "Import or update products from a CSV file (matches existing products by name)."

    def add_arguments(self, parser):
        parser.add_argument("csv_path", nargs="?", default="electronics_products_100.csv")

    def handle(self, *args, **options):
        path = Path(options["csv_path"]).expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.is_file():
            raise CommandError(f"CSV file not found: {path}")

        required = {"name", "category", "description", "price", "stock", "image_url"}
        created = updated = skipped = 0
        with path.open("r", encoding="utf-8-sig", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
                raise CommandError("CSV must contain columns: " + ", ".join(sorted(required)))
            for row_num, row in enumerate(reader, start=2):
                name = (row.get("name") or "").strip()
                if not name:
                    self.stderr.write(f"Row {row_num}: skipped because name is empty.")
                    skipped += 1
                    continue
                try:
                    price = Decimal((row.get("price") or "").strip())
                    stock = int((row.get("stock") or "").strip())
                    if price < 0 or stock < 0:
                        raise ValueError
                except (InvalidOperation, ValueError):
                    self.stderr.write(f"Row {row_num}: skipped because price or stock is invalid.")
                    skipped += 1
                    continue
                defaults = {
                    "category": (row.get("category") or "General").strip() or "General",
                    "description": (row.get("description") or "").strip(),
                    "price": price,
                    "stock": stock,
                    "image_url": (row.get("image_url") or "").strip(),
                }
                _, was_created = Product.objects.update_or_create(name=name, defaults=defaults)
                if was_created:
                    created += 1
                else:
                    updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Import complete. Created: {created}; updated: {updated}; skipped: {skipped}."
        ))
