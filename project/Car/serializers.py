from rest_framework import serializers
from .models import Order  

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'name', 'email', 'phone', 'address', 'city', 'cars', 'days_for_rent', 'date', 'loc_from', 'loc_to']
