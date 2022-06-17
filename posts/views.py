from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import *
from .forms import *

from .forms import SignUpForm, LogInForm

# Create your views here.
def home(request):
    
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()   
    return render(request, 'users/signup.html', {'form': form})


def log_in(request):
    error = False
   
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)  
                return redirect('home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'users/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('login'))

def profile(request, username):
  
    
   return render(request, 'profile.html')

def editProfile(request,username):
    user = CustomUser.objects.get(username=username)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            return redirect('profile',username=username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'edit_profile.html', context)