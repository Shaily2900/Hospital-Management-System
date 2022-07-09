from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index , name='home'),
    path('aboutus', views.aboutus , name='aboutus'),
    # path('admin', admin.site.urls , name='admin'),
    path('doctor', views.doctor , name='doctor'),
    path('patient', views.patient , name='patient'),
    path('signup', views.user_register , name='signup'),
    ]
