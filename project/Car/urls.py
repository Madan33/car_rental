from .views import BookingListView, BookingDetailView, BookingCreateView, BookingUpdateView, BookingDeleteView
from django.contrib import admin
from django.urls import path
from Car import views
from .views import * 


urlpatterns = [
    
    path("",views.index, name = 'home'),
    path("home/",views.index, name = 'home'),
    path("about/",views.about,name = 'about'),
    path("vehicles", views.vehicles, name= "vehicles"),
    path("bill",views.order,name = "bill"),
    path("contact/",views.contact,name = 'contact'),
    path("vehicles",views.Order,name = 'vehicles'),

    # Registration login and logout
    path("register/", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),

    #SHow Booking
    path('show_bookings',views.show_bookings,name='show_bookings'),

    #Rent
    path('rent_car/<int:pk>/', views.rent_car, name='rent_car'),
    path('rent/success/', views.rent_success, name='rent_success'),
    path('rented-cars/', views.rented_cars, name='rented_cars'),

    # Ride
    path('ride_list/', views.ride_list, name='ride_list'),
    path('ride_detail/<int:pk>/', views.ride_detail, name='ride_detail'),
    path('ride_request/', views.ride_request, name='ride_request'),
    path('ride/<int:pk>/update/', views.ride_update, name='ride_update'),
    path('ride_accept/<int:ride_id>/', views.ride_accept, name='ride_accept'),
    path('ride/create/<int:vehicle_id>/',views.create_ride,name='create_ride'),

    #Book Vahicle
    path('book/<int:vehicle_id>/', views.book_vehicle, name='book_vehicle'),
    path('booking/', views.booking_detail, name='booking_detail'),

    


    path('rent/create/', views.rent_create_view, name='rent-create'),
    path('rent/<int:pk>/update/', views.rent_update_view, name='rent-update'),
    path('rent/<int:pk>/delete/', views.rent_delete_view, name='rent-delete'),


    #Vehile
    path('vehicle_list/', views.vehicle_list, name='vehicle_list'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/new/', views.vehicle_create, name='vehicle_create'),
    path('vehicle_edit/<int:pk>/', views.vehicle_update, name='vehicle_update'),
    path('vehicle_delete/<int:pk>/', views.vehicle_delete, name='vehicle_delete'),
   


    #Booking classbased view
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/new/', BookingCreateView.as_view(), name='booking-create'),
    path('bookings/<int:pk>/edit/', BookingUpdateView.as_view(), name='booking-update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'),
]



    











    
    
    