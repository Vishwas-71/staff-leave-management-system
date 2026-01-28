from django.urls import path 
from account import views
from leave.views import *


urlpatterns = [
    path('apply/' , apply_leave , name='apply_leave'),
    path('my_leaves/' ,my_leaves , name='my_leaves'),
    path('view_leaves/' ,view_leaves , name='view_leaves'),
    path('approve_leave/<int:id>/' ,approve_leave , name='approve_leave'),
    path('reject_leave/<int:id>/' ,reject_leave , name='reject_leave'),
]