from django.contrib import admin
from .models import Contact, Departments,Doctors,Booking

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)


class BookingAdmin(admin.ModelAdmin):

    list_display = ('id','patient_name','patient_phone','patient_email','doc_name','booking_date','booked_on')


admin.site.register(Booking,BookingAdmin)


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id','name','email','message')


admin.site.register(Contact,ContactAdmin)