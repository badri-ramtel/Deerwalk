from django.urls import path
from training_app import views


urlpatterns = [
    path('training/home', views.home),
    path('training/course', views.course)
]