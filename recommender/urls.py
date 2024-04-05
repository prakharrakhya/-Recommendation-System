
from django.contrib import admin
from django.urls import path 
from movieRecommender.views import *
from core.views import *

urlpatterns = [
    #core-------------
    path('admin/', admin.site.urls),
    #path('' , core_home , name= 'core_home'),
    path('login/' , login , name = 'login'),
    path('register/' , register , name='register'),
    path('dashboard/' , dashboard , name= 'dashboard'),
    path('logout/' , user_logout , name='logout'),
    #----------------
    
    #movie---------------
    path('' , movie_home , name='movieHome'),
    path('movie_area/search/' , movie_search , name='movieSearch'),
    path('movie_area/movie/' , movie_view_details , name = 'movieDetails' )
    #--------------------
]
