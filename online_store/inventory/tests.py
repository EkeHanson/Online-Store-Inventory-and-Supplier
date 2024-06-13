# inventory/tests.py

from django.test import TestCase
from .models import Item, Supplier

class InventoryTestCase(TestCase):
    def setUp(self):
        supplier1 = Supplier.objects.create(name="Supplier 1", contact_information="123 Street")
        item1 = Item.objects.create(name="Item 1", description="A test item", price=10.00)
        item1.suppliers.add(supplier1)

    def test_item_creation(self):
        item = Item.objects.get(name="Item 1")
        self.assertEqual(item.description, "A test item")
        self.assertEqual(item.price, 10.00)
        self.assertEqual(item.suppliers.count(), 1)
