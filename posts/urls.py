from django.urls import path
from . import views
from posts import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.log_in, name='login'),
  path('logout/', views.log_out, name='logout'),
  path('profile/<str:username>/',views.profile,name='profile'),
  path('edit_profile/<str:username>', views.editProfile, name='edit_profile'),
  path('new_hood/', views.new_hood, name='new_hood'),
  path('hood/', views.hood, name='hood'),
  path('edithood/', views.edit_hood, name='edithood'),
  path('businesses/<id>', views.businesses, name='hoodbusiness'),
  path('post', views.post, name='post'),
  path('edithood/', views.edit_hood, name='edithood'),
  path('hoodupdates/<id>', views.hoodupdates, name='hoodupdates'),
  path('joinhood/<id>', views.joinhood, name='joinhood'),
  path('leavehood/<id>', views.leavehood, name='leavehood'),
  path('singlehood/<id>', views.singlehood, name='singlehood'),
  path('search/', views.search_business, name='search'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
