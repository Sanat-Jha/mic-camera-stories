from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', aboutus, name='about'),
    path('yourstory', yourstory, name='yourstory'),
    path('stories', stories, name='stories'),
    path('story', story, name='story'),
    path('databaserefresh', databaserefresh, name='databaserefresh'),
]
