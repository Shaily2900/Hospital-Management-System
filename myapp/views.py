from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Patient
# Create your views here.
def index(request):
    user=request.user

    print(f'+++++++++++++++++++++++++++++{user}      {type(user)}+++++++++++++++++++')
    context = {
        'variable': 'this is sent','user':str(user)}
    return render(request,'index.html',{'data':context})
    # return HttpResponse('This is homepage')
def aboutus(request):
    return render(request,'aboutus.html')
    # return HttpResponse('This is about us page')
# def admin(request):
#     # return render(request,'aboutus.html')
    # return HttpResponse('This is admin page')
def doctor(request):
    # return render(request,'cart.html')
    return HttpResponse('This is a doctor page')
def patient(request):
    # return render(request,'payment.html')
    return HttpResponse('This is a patient page')
def signup(request):
    return render(request,'signup.html')
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'signup.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.age = form.cleaned_data['age']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                patient = Patient.objects.create(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username=form.cleaned_data['username'],email=form.cleaned_data['email'],age=form.cleaned_data['age'],phone_number=form.cleaned_data['phone_number'])
                patient.save()
                # Login the user
                # login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('admin/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
