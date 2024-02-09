from django.urls import path
from . import views

urlpatterns = [
    path("submit/", views.submit_all, name="submit_all"),
]
