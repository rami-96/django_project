from cProfile import label
from django import forms
from .models import Booking,Contact


class DateInput(forms.DateInput):
    input_type ='date'


class BookingForm(forms.ModelForm):


    class Meta:
        model = Booking
        fields = '__all__'


        widgets = {
            'booking_date' : DateInput()
        }


        labels = {

            'patient_name':"Patient Name: ",
            'patient_phone' : "Patient Phone: ",
            'patient_email':"Patient Email:",
            'doc_name':"Doctor Name: ",
            'booking_date':"Booking Date: ",
        }



class ContactUs(forms.ModelForm):


    class Meta:
        model = Contact
        fields = '__all__'

        labels = {

            'name':"Your name",
            'email':"Your email",
            'message':"Your message",
        }



        