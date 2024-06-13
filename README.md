# Online Store Inventory and Supplier Management API

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt



Run migrations:
bash
Copy code
python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser

Run the server: 
python manage.py runserver

Endpoints
/api/items/ - CRUD operations for inventory items.
/api/suppliers/ - CRUD operations for suppliers.

Running Tests: To run tests, use:
python manage.py test