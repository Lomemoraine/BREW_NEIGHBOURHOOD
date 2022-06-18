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