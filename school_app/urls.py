from django.urls import path
from school_app import views


urlpatterns = [
    path('school/home',views.home)
]