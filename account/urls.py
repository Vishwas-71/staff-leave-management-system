from django.urls import path 
from account.views import *

urlpatterns = [
    path('',home , name='home'),
    path('register/' , register , name = "register") , 
    path('login/' , login_view , name="login"),
    path('staff_dashboard/' , staff_dashboard , name='staff_dashboard'),
    path('admin_dashboard/' , admin_dashboard , name='admin_dashboard'),
    path('logout/' , logout_view , name='logout' )
  
]