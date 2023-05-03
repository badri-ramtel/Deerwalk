from django.shortcuts import render
from training_app.models import UpcomingClass, Course

# Create your views here.
def home(request):
    classes = UpcomingClass.objects.all()
    return render(request, 'training_app/home.html', {'classes' : classes})

def courses(request):
    courses = Course.objects.filter(title__iexact = 'Java') # all().order_by('-price', 'title')
    return render(request, 'training_app/courses.html', {'courses' : courses})

def add_course(request):
    return render(request, 'training_app/add_course.html')
