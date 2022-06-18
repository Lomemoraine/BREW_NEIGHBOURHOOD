from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, NewHoodForm, EditHoodForm, NewBizForm, NewPostForm
from .models import Profile, Neighbourhood, Business, Post

# Create your views here.
def home(request):
    
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})