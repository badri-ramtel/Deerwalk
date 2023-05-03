from django.urls import path
from college_app import views


urlpatterns = [
    path('college/home', views.home)
]
