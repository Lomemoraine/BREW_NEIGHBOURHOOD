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

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f'Your account has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }

    return render(request, 'update_profile.html', context)

@login_required(login_url='/accounts/login/')
def hood(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods.html', {"hoods": hoods})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.admin = current_user.profile

            image.save()

        return redirect('hood')

    else:
        form = NewHoodForm()
    return render(request, 'new_hood.html', {"form": form})

def edit_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditHoodForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            image = form.save(commit=False)
            image.admin = current_user.profile

            image.save()
        return redirect('hood')

    else:
        form = EditHoodForm()
    return render(request, 'edit_hood.html', {'form': form})

def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('hood')

def leavehood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='/accounts/login/')
def singlehood(request, id):
    hood = Neighbourhood.objects.get(id=id)
    return render(request, 'singlehood.html', {'hood':hood})

@login_required(login_url='/accounts/login/')
def businesses(request, id):
    business = Business. hood_hustle(id=id)
    return render(request, 'business.html', {'business': business})

@login_required(login_url='/accounts/login/')
def newbiz(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBizForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user

            business.save()

        return redirect('hood')

    else:
        form = NewBizForm()
    return render(request, 'newbiz.html', {"form": form})