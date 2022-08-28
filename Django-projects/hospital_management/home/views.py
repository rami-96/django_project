from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors,Contact
from .forms import BookingForm, ContactUs

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form = BookingForm()
    dict_form = {
        'form' : form
    }

    
    return render(request,'booking.html',dict_form)


def doctors(request):
    dict_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)


def contact(request):
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'message.html')
            

    form = ContactUs()

    dict_cont= {

        'form' : form
    }
    return render(request,'contact.html',dict_cont)


def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)