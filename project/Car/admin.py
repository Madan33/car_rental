from django.contrib import admin
from .models import *

# Register your models here.
class caradmin(admin.ModelAdmin):
    list_display=['car_id','car_name','car_desc','image','price']
admin.site.register(Car,caradmin)

class orderadmin(admin.ModelAdmin):
    list_display=['order_id','name','email','phone','address','city','cars','days_for_rent','date','loc_from','loc_to']
admin.site.register(Order,orderadmin)

class contactadmin(admin.ModelAdmin):
    name = models.CharField(max_length=150,default="")
    list_display=['name','email','phone_number','message']
admin.site.register(Contact,contactadmin)
admin.site.register(rent)
admin.site.register(Ride)
admin.site.register(Vehicle)
admin.site.register(Booking)
