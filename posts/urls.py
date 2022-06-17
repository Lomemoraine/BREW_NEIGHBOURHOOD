from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.log_in, name='login'),
  path('logout/', views.log_out, name='logout'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
