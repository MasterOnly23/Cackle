from unicodedata import name
from django.contrib import admin
from django.urls import path
from SocialMedia.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView #vistas predefinidas de django


urlpatterns = [
    path('', index, name='index'),
    path('feed/', feed, name='feed'),
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('post/', post, name='post'),
    path('edit_post/<int:id_post>/', edit_post, name='edit_post'),
    path('update_post/<int:id_post>/', update_post, name='update_post'),
    path('delete_post/<int:id_post>/', delete_post, name='delete_post'),
    path('follow/<str:username>/', follow, name='follow'),
    path('unfollow/<str:username>/', un_follow, name='unfollow'),  
    path('my_data', my_data, name='my_data'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('edit_avatar/', edit_avatar, name='edit_avatar'),
    path('edit_pass/', edit_pass, name='edit_pass'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
