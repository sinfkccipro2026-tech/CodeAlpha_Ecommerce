# ShopEase — Django E-commerce (VS Code)

A Django 5.2 storefront with a refreshed responsive green-and-white UI, CSS-built hero artwork, shopping benefits, product search/category filtering, product details, session cart, registration/login, checkout demo, and order history.

## Requirements
- Windows 10/11
- Python 3.10 or newer (`py --version` should work)
- VS Code
- Internet connection during package installation; product photos use external Unsplash URLs

## IMPORTANT: run this extracted copy on port 8010
If an older ShopEase website is already running on `127.0.0.1:8000`, it can make you think the new files have not changed. This project is configured to run on **http://127.0.0.1:8010/** in the steps below. Always open that exact URL for this extracted copy.

## Run in VS Code (Windows PowerShell)
1. Download and extract the ZIP using **Extract All**.
2. In VS Code, choose **File → Open Folder** and select the extracted `CodeAlpha_Ecommerce` folder (the one containing `manage.py`).
3. Choose **Terminal → New Terminal**.
4. Check the folder:
   ```powershell
   dir
   ```
   You should see `manage.py`, `requirements.txt`, `shop`, and `store`.
5. Create a virtual environment (one time):
   ```powershell
   py -m venv venv
   ```
6. Install Django:
   ```powershell
   .\venv\Scripts\python.exe -m pip install -r requirements.txt
   ```
7. Apply database migrations:
   ```powershell
   .\venv\Scripts\python.exe manage.py migrate
   ```
8. Add sample products:
   ```powershell
   .\venv\Scripts\python.exe manage.py seed_products
   ```
9. Start this copy on port 8010:
   ```powershell
   .\venv\Scripts\python.exe manage.py runserver 127.0.0.1:8010
   ```
10. Open **http://127.0.0.1:8010/** in Edge or Chrome. Keep the terminal open while using the website.

If PowerShell says the path does not exist, use quotes around paths containing spaces. For example:
```powershell
cd "C:\Users\Sheela C M\Downloads\ShopEase_Complete_Fixed\CodeAlpha_Ecommerce"
```

## Admin account (optional)
Open a second terminal in the same project folder and run:
```powershell
.\venv\Scripts\python.exe manage.py createsuperuser
```
Then open http://127.0.0.1:8010/admin/.

## If the UI still looks old
- Confirm the browser address is **127.0.0.1:8010**, not 8000.
- Confirm VS Code terminal path is the extracted `CodeAlpha_Ecommerce` folder.
- Press **Ctrl + Shift + R** to refresh.
- Open http://127.0.0.1:8010/static/shop/css/style.css; you should see CSS text.

## Notes
- The SQLite database is created locally after migrations; this ZIP intentionally does not include a personal database or virtual environment.
- Checkout records a demo order and does **not** connect to a real payment gateway.
- This is a local development project, not production-hardened deployment configuration.
