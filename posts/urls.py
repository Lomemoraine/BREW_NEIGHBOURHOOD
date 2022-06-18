from django.urls import path
from . import views
from posts import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', user_views.update_profile, name='update_profile'),
    path('new_hood/', views.new_hood, name='new_hood'),
    path('hood/', views.hood, name='hood'),
    path('edithood/', views.edit_hood, name='edithood'),
    path('businesses/<id>', views.businesses, name='hoodbusiness'),
    path('post', views.post, name='post'),
    path('hoodupdates/<id>', views.posthood, name='hoodupdates'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
