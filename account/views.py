from django.shortcuts import render , redirect
from account.models import Profile
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate   , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return render(request , 'home.html')

def register(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    role = request.POST['role']
    user = User.objects.create_user(username=username , password=password)
    Profile.objects.create(user=user , role=role)
    return redirect('login')
  return render(request , 'register.html')

def login_view(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user  = authenticate(request , username=username , password=password)
    if user:
      login(request , user)
      if user.profile.role == 'admin':
        return redirect('admin_dashboard')
      else:
        return redirect('staff_dashboard')
  return render(request , 'login.html')


@login_required
def staff_dashboard(request):
  return render(request , 'staff_dashboard.html')

@login_required
def admin_dashboard(request):
  if request.user.profile.role != 'admin':
    return redirect('staff_dashboard')
  return render(request , 'admin_dashboard.html')

def logout_view(request):
  logout(request)
  return redirect('home')