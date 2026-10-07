from django.core.management.base import BaseCommand
from shop.models import Product

PRODUCTS=[
('Wireless Headphones','Electronics','Comfortable Bluetooth headphones with clear sound and long battery life.',2499,'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800',15),
('Smart Watch','Electronics','Fitness tracking, notifications and a bright touch display.',3299,'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800',12),
('Running Shoes','Fashion','Lightweight everyday running shoes with a cushioned sole.',1899,'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800',20),
('Backpack','Fashion','Durable laptop backpack for college, work and travel.',1299,'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800',18),
('Coffee Maker','Home','Compact coffee maker for quick and fresh coffee at home.',2799,'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800',10),
('Desk Lamp','Home','Minimal LED desk lamp with adjustable brightness.',899,'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800',25),
]
class Command(BaseCommand):
    help='Create demo products'
    def handle(self,*args,**kwargs):
        for name,cat,desc,price,img,stock in PRODUCTS:
            Product.objects.update_or_create(name=name,defaults={'category':cat,'description':desc,'price':price,'image_url':img,'stock':stock})
        self.stdout.write(self.style.SUCCESS('Demo products created.'))
