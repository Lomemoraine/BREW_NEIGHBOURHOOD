from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.James = User(username ='James',email='james@gmail.com')
        self.James = Profile(user = self.james,user_id=1,bio = 'my hood', email='james@gmail.com',profile_pic = 'image.jpg',location='Mombasa', neighbourhood='Tudor')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.james.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

class BusinessTestCase(TestCase):
    self.new_neighborhood= Project(name = 'market',user = 'James',email = 'james@gmail',neighborhood = 'Nyali',descrption='serenity at its best')


    def test_save_image(self):
        self.name.save_name()
        name = Business.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.name.save_image()
        self.name.delete_image()
        image_list = Business.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.name.save_name()
        all_names = Business.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.pet.save_image()
        one_name = Business.get_one_name(self.pet.id)
        self.assertTrue(one_name.name == self.name.name)

class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new_neighborhood= Project(name ='Tudor',location = 'Mombasa',image = 'image.jpg',description = 'lovely hood',user = james,emergency_contact= '911',occupants_count ='8')

    def test_save_image(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        image_list = Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.image.save_image()
        all_images = Image.get_all_images()
        self.assertTrue(len(all_pictures) < 1)

    def test_get_one_image(self):
        self.pet.save_image()
        one_pic = Image.get_one_image(self.pet.id)
        self.assertTrue(one_pic.name == self.picture.name)

class PostTestCase(TestCase):
    self.new_neighborhood= Project(title = 'hood',User = 'James',text = 'serenity at its best',date_created='June,18,2022')
    def test_save_image(self):
        self.name.save_name()
        name = Business.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.name.save_name()
        self.name.delete_image()
        image_list = Business.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.name.save_image()
        all_names = Business.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.pet.save_image()
        one_name = Business.get_one_name(self.pet.id)
        self.assertTrue(one_name.name == self.name.name)                        