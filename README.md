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

5. create super user:< br / >

python manage.py createsuperuser

6. Run the server: < br / >

python manage.py runserver< br / >

Endpoints:< br / >

/api/items/ - CRUD operations for inventory items.< br / >
/api/suppliers/ - CRUD operations for suppliers.< br / >

5. Running Tests: To run tests, use:< br / >
python manage.py test