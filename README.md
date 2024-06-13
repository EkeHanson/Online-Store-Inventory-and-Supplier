# Online Store Inventory and Supplier Management API

## Setup

1. Clone the repository.

git clone https://github.com/EkeHanson/Online-Store-Inventory-and-Supplier.git

2. Install dependencies:

pip install -r requirements.txt

3. Run migrations:

python manage.py makemigrations

4. Migrate the  migrations:

python manage.py migrate

5. create super user:

python manage.py createsuperuser


6. Run the server: 

python manage.py runserver

Endpoints

/api/items/ - CRUD operations for inventory items.

/api/suppliers/ - CRUD operations for suppliers.


5. Running Tests: To run tests, use:

python manage.py test