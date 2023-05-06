from django.urls import path
from training_app import views


urlpatterns = [
    path('', views.home, name='training-home'),
    path('courses/', views.courses, name='training-courses'),
    path('home/', views.home),
    path('add-course/', views.add_course, name='training-add-course'),
    path('delete/<int:id>/', views.delete, name='training-delete'),
    path('edit/<int:id>', views.edit, name='training-edit')
]