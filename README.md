# CodeAlpha E-commerce Store

A complete Django e-commerce project for the CodeAlpha Full Stack Development Task 1.

## Included
- Product listing and search/filter
- Product details page
- Session-based shopping cart
- Quantity update/remove
- User registration/login/logout
- Checkout and order processing
- User order history
- SQLite database
- Django admin for products and orders
- Responsive HTML/CSS/JavaScript UI

## Requirements
- Python 3.10+
- pip

## Windows setup
```bat
cd CodeAlpha_Ecommerce
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py seed_products
py manage.py createsuperuser
py manage.py runserver
```

Open http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

## Demo flow
1. Register a user.
2. Browse products.
3. Open a product and add it to cart.
4. Update cart quantity.
5. Checkout with delivery details.
6. View the order under My Orders.

The checkout is a demo order flow; no real payment gateway is connected.

## Task mapping
Task 1 requires product listings, shopping cart, product details, order processing, user registration/login, and a database for products/users/orders. This project implements those requirements using Django + SQLite.
