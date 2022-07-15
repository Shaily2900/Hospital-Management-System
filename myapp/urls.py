from django.urls import path 
from myapp import views 


urlpatterns = [
    path('', views.index , name='home'),
    path('aboutus/', views.aboutus , name='aboutus'),
    path('admin/', views.admin, name='admin'),
    path('admin_register/', views.admin_register),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient , name='patient'),
    # path('signup/', views.user_register , name='signup'),
    ]
