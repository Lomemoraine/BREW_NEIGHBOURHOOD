from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic','f_name','l_name','phone','bio']
        
class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)

class EditHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)

class NewBizForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user',)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)