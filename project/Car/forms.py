from django import forms
from .models import rent,Ride,Booking,Vehicle,Car

class RentForm(forms.ModelForm):
    class Meta:
        model = rent
        fields = ['customer_name', 'phone', 'car']
        # Add more fields as needed


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['passenger', 'driver', 'start_location', 'end_location', 'status']

class carform(forms.ModelForm):
    class Meta:
        model=Car
        fields=['car_id','image','car_name','car_desc','price']
        


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user_name', 'email', 'phone_number', 'pickup_date', 'dropoff_date']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'vehicle_type', 'description', 'rate_per_day']