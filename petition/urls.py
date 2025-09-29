from django.urls import path
from . import views

app_name = "petition"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.show, name="show"),
    path("create/", views.create, name="create"),
    path("<int:id>/vote/", views.vote, name="vote"),
]
