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
        self.save_profile()
        self.james.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

class BusinessTestCase(TestCase):
    def setUp(self):
        self.new_business = Business(user='james',neighbourhood='Tudor',description='lovely hood')
    
    def test_save_business(self):
        self.save_business()
        business = Business.objects.all()
        self.assertEqual(len(business),1)

    def test_delete_business(self):
        self.save_business()
        self.delete_business()
        business_list = Business.objects.all()
        self.assertTrue(len(business)==0)

    def test_get_all_business(self):
       
        self.save_business()
        all_business = Business.get_all_business()
        self.assertTrue(len(all_business) < 1)

    

class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new_neighbourhood= Neighbourhood(title ='Tudor',location = 'Mombasa',description = 'lovely hood',user = james,emergency_contact= '911',occupants_count ='8')

    def test_save_neighbourhood(self):
        self.save_neighbourhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertEqual(len(neighbourhood),1)

    def test_delete_neighbourhood(self):
        self.save_neighbourhood()
        self.delete_neighbourhood()
        neighbourhood_list = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood)==0)

    def test_get_all_neighbourhoods(self):
       
        self.save_neighbourhood()
        all_neighbourhoods = Neighbourhood.get_all_neighbourhoods()
        self.assertTrue(len(all_neighbourhoods) < 1)

    def test_get_one_neighbourhood(self):
        self.house.save_neighbourhood()
        one_neighbourhood = Neighbourhood.get_one_neighbourhood(self.house.id)
        self.assertTrue(one_neighbourhood.neighbourhood == self.neighbourhood.neighbourhood)

class PostTestCase(TestCase):
    def setUp(self):
        self.new_post=Post(user='james',neighbourhood='Tudor',title='my new hood',date_created='18.06.22')
   
    def test_save_post(self):
        self.save_post()
        post = Post.objects.all()
        self.assertEqual(len(posts),1)

    def test_delete_post(self):
        self.save_post()
        self.delete_post()
        post_list = Post.objects.all()
        self.assertTrue(len(post)==0)

    def test_get_all_posts(self):
       
        self.save_post()
        all_posts = Post.get_all_posts()
        self.assertTrue(len(all_posts) < 1)

    def test_get_one_post(self):
        self.house.save_post()
        one_post = Post.get_one_post(self.house.id)
        self.assertTrue(one_post.post == self.post.post)                        