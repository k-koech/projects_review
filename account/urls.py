from account.serializer import MerchUser
from django.contrib import admin
from django.urls import path
from .views.auth import index, register,signIn, signOut
from .views.projects import add_project,profile, profile_photo,MerchList, MerchUsers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', signIn, name='login'),
    path('signOut', signOut, name='signOut'),

    path('profile', profile, name='profile'),
    path('profile_photo', profile_photo, name='profile_photo'),
    path('add_project', add_project, name='add_project'),

    # API
    path('api/users/', MerchUsers.as_view()),
    path('api/projects/', MerchList.as_view()),
    path('api/api-token-auth/', obtain_auth_token)

    
]
