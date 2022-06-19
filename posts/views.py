

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *




# Create your views here.
def home(request):
    

    return render(request, 'home.html')




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



@login_required(login_url='login/')
def hood(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods.html', {"hoods": hoods})

@login_required(login_url='login/')
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

@login_required(login_url='login/')
def singlehood(request, id):
    hood = Neighbourhood.objects.get(id=id)
    return render(request, 'singlehood.html', {'hood':hood})

@login_required(login_url='login/')
def businesses(request, id):
    business = Business. hood_hustle(id=id)
    return render(request, 'business.html', {'business': business})

@login_required(login_url='login/')
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

@login_required(login_url='login/')
def hoodupdates(request, id):
    post = Post.hood_updates(id=id)
    return render(request, 'hoodupdates.html', {'post': post})
@login_required(login_url='login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user

            post.save()

        return redirect('hood')

    else:
        form = NewPostForm()
    return render(request, 'post.html', {"form": form})

def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("name")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any business"
    return render(request, 'results.html', {'message': message})
