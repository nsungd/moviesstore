from django.urls import path
from . import views

app_name = 'settingsapp'

urlpatterns = [
    path('security/', views.update_security_settings, name='update_security'),
    path('', views.index, name='index'),
]
