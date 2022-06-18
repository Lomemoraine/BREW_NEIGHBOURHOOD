from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=100, blank =True )
    bio = models.TextField(max_length=300,blank =True)
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='profile')
    email = models.CharField(max_length=100, default = '')
    location = models.CharField(max_length=100,blank =True)
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save_profile(self):
        self.save
    
    def delete_user(self):
        self.delete()
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        
class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location= models.CharField(max_length=60)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE, related_name = 'hood')
    description = models.TextField( default = '')
    hood_logo = models.ImageField( upload_to='images/', blank ='true',default='')
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
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    email = models.CharField(max_length=100, default = '')
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    description = models.TextField( default = '')
    
    def __str__(self):
        return f'{self.name} business'
    
    def save_business(self):
            self.save()

    def delete_business(self):
        self.delete()