from django import forms
from django.shortcuts import render, redirect
from .forms import AdminSignupForm
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse('This is homepage')
def aboutus(request):
    return render(request,'aboutus.html')
    # return HttpResponse('This is about us page')
def admin(request):
    return render(request,'admin_base.html')
def doctor(request):
    return render(request,'doctor_base.html')
    # return HttpResponse('This is a doctor page')
def patient(request):
    return render(request,'patient_base.html')
    # return HttpResponse('This is a patient page')


def admin_register(request):
    form=forms.AdminSignupForm()
    if request.method=='POST':
        form=AdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_register')
    return render(request,'admin_register.html',{'form':form})
