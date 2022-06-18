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