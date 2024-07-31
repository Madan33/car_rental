from email.policy import default
from django.db import models
from django.utils import timezone
from .models import *
import datetime

class Car(models.Model):
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30,default="")
    car_desc = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images",default="")
    


    def __str__(self):
        return self.car_name

class Order(models.Model) :
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    cars = models.CharField(max_length=50,default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50,default="")
    loc_from = models.CharField(max_length=50,default="")
    loc_to = models.CharField(max_length=50,default="")

    completed = models.BooleanField(default=False)
    completion_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.order_id}"

    def mark_completed(self):
        self.completed = True
        self.completion_date = timezone.now().date()
        self.save()
    
  

class Contact(models.Model):
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name



class rent(models.Model):
    customer_name=models.CharField(max_length=100, default=0)
    phone=models.CharField(max_length=100,default=0)
    car = models.ForeignKey('Car', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Rental ID: {self.id} - Customer: {self.customer_name}"
    




class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('bike', 'Bike'),
        ('auto', 'Auto'),
        ('car', 'Car'),
    )
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    description = models.TextField()
    rate_per_day = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.get_vehicle_type_display()} - {self.name}"

class Ride(models.Model):
    passenger = models.CharField(max_length=250)
    driver = models.CharField(max_length=250, blank=True)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    date_requested = models.DateTimeField(auto_now_add=True)
    date_accepted = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
   


    def __str__(self):
        return f"Ride ID: {self.id} - Passenger: {self.passenger}"

class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user_name} - {self.vehicle.name}'
    
