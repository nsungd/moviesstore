from django.urls import path
from . import views

app_name = 'liked'

urlpatterns = [
    path('', views.index, name='index'),  # points to the index function
]
