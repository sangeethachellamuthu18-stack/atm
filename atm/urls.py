from django.urls import path
from . import views
from . views import Loginpage,Registerpage,Dashboard


urlpatterns = [
    path('',Loginpage,name='loginpage'),
    path('register/',Registerpage,name="registerpage"),
    path('dashboard',Dashboard,name="dashboard"),

]