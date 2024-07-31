from .models import Car, Order, Contact,rent,Vehicle,Booking
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, get_object_or_404
from .forms import RentForm,RideForm,BookingForm,VehicleForm,carform
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.views import APIView
from .serializers import OrderSerializer
from rest_framework import serializers
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import status
from django.utils import timezone
from .models import  Ride
import datetime

def index(request):
	return render(request,'home/index.html')

# About car
def about(request):
    return render(request,'home/about.html')

 # Register
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).first():
            messages.error(request,"Username already taken")
            return redirect('register')
        if User.objects.filter(email = email).first():
            messages.error(request,"Email already taken")
            return redirect('register')

        if password != password2:
            messages.error(request,"Passwords do not match")
            return redirect('register')

        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.name = name
        myuser.save()
        messages.success(request,"Your account has been successfully created!")
        return redirect('signin')


    else:
        print("error")
        return render(request,'login/register.html')
    
# Signin
def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            return redirect('vehicles')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')

    else:
        print("error")
        return render(request,'login/login.html')
    
# Signout
def signout(request):
        logout(request)
        return redirect('home')
    

# All vehicles List
def vehicles(request):
    context={}
    context['vehicles'] = Car.objects.all()
    return render(request,'vehicle/vehicles.html',context)

def vehicle_list(request):
    vehicles = Car.objects.all()
    return render(request, 'vehicle/curd/vehicle_list.html', {'vehicles': vehicles})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Car, pk=pk)
    return render(request, 'vehicle/curd/ vehicle_detail.html', {'vehicle': vehicle})


def vehicle_create(request):
    if request.method == 'POST':
        form = carform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  
    else:
        form = carform()
    return render(request, 'vehicle/curd/vehicle_form.html', {'form': form})

def vehicle_update(request, pk):
    vehicle = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = carform(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = carform(instance=vehicle)
    return render(request, 'vehicle/curd/vehicle_form.html', {'form': form})

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicle/curd/vehicle_confirm_delete.html', {'vehicle': vehicle})

# order the car
def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        billcity = request.POST.get('billcity','')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss','')
        date = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')
        
        
        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,city=billcity,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request,'bill/bill.html')

# Cntact
def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname','')
        contactemail = request.POST.get('contactemail','')
        contactnumber = request.POST.get('contactnumber','')
        contactmsg = request.POST.get('contactmsg','')

        contact = Contact(name = contactname, email = contactemail, phone_number = contactnumber,message = contactmsg)
        contact.save()
    return render(request,'contact/contact.html')

# About Booking
def show_bookings(request):
    bookings = Order.objects.all()  
    paginator = Paginator(bookings, 2)  

    page = request.GET.get('page')
    try:
        bookings = paginator.page(page)
    except PageNotAnInteger:
        
        bookings = paginator.page(1)
    except EmptyPage:
        
        bookings = paginator.page(paginator.num_pages)

    return render(request, 'vehicle/bookings.html', {'bookings': bookings})


# About rent car
def rent_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            phone = form.cleaned_data['phone']
            car.customer_name = customer_name
            car.phone = phone
            car.save()
            return redirect('rent_success') 
    else:
        form = RentForm()
    
    return render(request, 'rent/rent.html', {'car': car, 'form': form})

def rent_success(request):
    return render(request, 'rent/rent_success.html')

# About who are rented for cars
def rented_cars(request):
    rented_cars = Car.objects.all()
    rented_car_instances = rent.objects.all()
    
    context = {
        'rented_cars': rented_cars,
        'rented_car_instances': rented_car_instances,
    }
    
    return render(request, 'rent/rented_cars.html', context)


# RIde
def ride_list(request):
    ride=Ride.objects.all()
    return render (request,'ride/ride_list.html',{"ride":ride})

def ride_detail(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    return render(request, 'ride/ride_detail.html', {'ride': ride})

def create_ride(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.vehicle = vehicle  
            ride.save()
            return redirect('ride_detail', ride_id=ride.id)  
        form = RideForm()
    
    context = {
        'form': form,
        'vehicle': vehicle,
    }
    return render(request, 'ride/ride_create.html', context)

def ride_request(request):
    if request.method == 'POST':
        passenger = request.POST.get('passenger')
        start_location = request.POST.get('start_location')
        end_location = request.POST.get('end_location')
        date_requested = timezone.now()

        try:
            ride = Ride.objects.get(passenger=passenger,
                start_location=start_location,
                end_location=end_location,
                date_requested=date_requested,
            )
            return redirect('ride_detail', pk=ride.pk)
        
        except Ride.DoesNotExist:
           
            ride = Ride.objects.create(
                passenger=passenger,
                start_location=start_location,
                end_location=end_location,
                date_requested=date_requested,
            )
            
            return redirect('ride_detail', pk=ride.pk)
     
    return render(request, 'ride/ride_request.html')

def ride_accept(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)

    if request.method == 'POST':
        if ride.status == 'requested':  
            ride.driver = request.POST.get('driver')
            ride.status = 'accepted'
            ride.date_accepted = timezone.now()
            ride.save()
            return redirect('ride_detail', ride_id=ride.id) 
    return render(request, 'ride/ride_accept.html', {'ride': ride})


def ride_update(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if request.method == "POST":
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            ride = form.save()
            return redirect('ride_detail', pk=ride.pk)
    else:
        form = RideForm(instance=ride)
    return render(request, 'ride/ride_update.html', {'form': form})



# Booking
def book_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.vehicle = vehicle
            booking.total_amount = (booking.dropoff_date - booking.pickup_date).days * vehicle.rate_per_day
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
        else:
            return render(request, 'book_vehicle/book_vehicle.html', {'form': form, 'vehicle': vehicle})

    else:
        form = BookingForm()
    return render(request, 'book_vehicle/book_vehicle.html', {'form': form, 'vehicle': vehicle})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'book_vehicle/booking_confirmation.html', {'booking': booking})


def booking_detail(request):
    booking = Booking.objects.all()
    return render(request, "book_vehicle/booking_detail.html", {'booking': booking})



# Rent create 
def rent_create_view(request):
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rent_success') 
    else:
        form = RentForm()
    
    context = {
        'form': form
    }
    return render(request, 'rent/rent_create.html', context)


def rent_update_view(request, pk):
    rent_instance = get_object_or_404(rent, pk=pk)
    
    if request.method == 'POST':
        form = RentForm(request.POST, instance=rent_instance)
        if form.is_valid():
            form.save()
            return redirect('rent_success')  
    else:
        form = RentForm(instance=rent_instance)
    
    context = {
        'form': form
    }
    
    return render(request, 'rent/rent_update.html', context)


def rent_delete_view(request, pk):
    rent_instance = get_object_or_404(rent, pk=pk)
    
    if request.method == 'POST':
        rent_instance.delete()
        return redirect('rent_success')  
    
    context = {
        'rent_instance': rent_instance
    }
    return render(request, 'rent/rent_delete.html', context)





# Booking
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking


class BookingListView(ListView):
    model = Booking
    template_name = 'booking_class_based/booking_list.html' 
    context_object_name = 'bookings'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_class_based/booking_detail.html'  
    context_object_name = 'booking'

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'booking_class_based/booking_form.html'  
    fields = '__all__'  
    success_url = reverse_lazy('booking-list')  


class BookingUpdateView(UpdateView):
    model = Booking
    template_name = 'booking_class_based/booking_form.html'  
    fields = '__all__'  
    success_url = reverse_lazy('booking-list')  

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_class_based/booking_confirm_delete.html'  
    success_url = reverse_lazy('booking-list')  
