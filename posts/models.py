from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    prof_pic = CloudinaryField('images', default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.TextField(blank=True, max_length=255 ,default='please update your bio')
    f_name = models.CharField(blank=True, max_length=255)
    l_name = models.CharField(blank=True,max_length=50)
    phone = PhoneNumberField(blank=True)
    

    def __str__(self):
        return self.f_name

    def save_profile(self):
        '''Add Profile to database'''
        self.save()
        
class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location= models.CharField(max_length=60)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE, related_name = 'hood')
    description = models.TextField( default = '')
    hood_logo = CloudinaryField('images', default='')
    emergency_contact=models.CharField(max_length=100,null=True, blank=True)
    occupants_count = models.IntegerField(null  = True ,blank = True)
    
    def __str__(self):
        return f'{self.name} neighbourhood'
    
    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
        
class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default = '')
    email = models.CharField(max_length=100, default = '')
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    description = models.TextField( default = '')
    
    def __str__(self):
        return f'{self.name} business'
    
    def save_business(self):
            self.save()

    def delete_business(self):
        self.delete()
        
    @classmethod
    def hood_hustle(cls, id):
        hoodhustles = Business.objects.filter(neighbourhood = id)
        return hoodhustles
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default = '')
    date = models.DateField(auto_now_add=True)
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} Post'
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
    @classmethod
    def hood_updates(cls, id):
        hoodupdates = Post.objects.filter(neighbourhood = id)
        return hoodupdates

