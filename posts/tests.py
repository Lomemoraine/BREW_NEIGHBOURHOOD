from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.James = User(name ='James',bio='lovely hood')
        self.James = Profile(user = self.james,user_id=1,bio = 'lovely hood', prof_pic = 'image.jpg',location='Mombasa', neighbourhood='Tudor')
    
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
    def setUp(self):
        self.new_business = Business(user='james',neighbourhood='Tudor',description='lovely hood')
    
    def test_save_image(self):
        self.name.save_name()
        name = Business.objects.all()
        self.assertEqual(len(images),1)

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
        self.house.save_image()
        one_name = Business.get_one_name(self.house.id)
        self.assertTrue(one_name.name == self.name.name)

class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new_neighbourhood= Neighbourhood(title ='Tudor',location = 'Mombasa',description = 'lovely hood',user = james,emergency_contact= '911',occupants_count ='8')

    def test_save_image(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertEqual(len(image),1)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        image_list = Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.image.save_image()
        all_images = Image.get_all_images()
        self.assertTrue(len(all_images) < 1)

    def test_get_one_image(self):
        self.house.save_image()
        one_pic = Image.get_one_image(self.house.id)
        self.assertTrue(one_pic.name == self.image.name)

class PostTestCase(TestCase):
    def setUp(self):
        self.new_post=Post(user='james',neighbourhood='Tudor',title='my new hood',date_created='18.06.22')
   
    def test_save_image(self):
        self.name.save_name()
        name = Post.objects.all()
        self.assertEqual(len(images),1)

    def test_delete_image(self):
        self.name.save_name()
        self.name.delete_image()
        image_list = Post.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.name.save_image()
        all_names = Post.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.house.save_image()
        one_name = Post.get_one_name(self.house.id)
        self.assertTrue(one_name.name == self.name.name)                        