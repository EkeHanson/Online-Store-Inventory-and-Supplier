# inventory/serializers.py

from rest_framework import serializers
from .models import Item, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all(), required=False)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_information', 'items']

class ItemSerializer(serializers.ModelSerializer):
    suppliers = serializers.PrimaryKeyRelatedField(many=True, queryset=Supplier.objects.all())

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'suppliers']
