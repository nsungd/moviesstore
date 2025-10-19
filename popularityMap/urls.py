# popularityMap/urls.py
from django.urls import path
from . import views

app_name = 'popularityMap'  # important!

urlpatterns = [
    path('', views.popularity_map, name='index'),  # /map/
]