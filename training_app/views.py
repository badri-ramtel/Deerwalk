from django.shortcuts import render
from training_app.models import UpcomingClass

# Create your views here.
def home(request):
    classes = UpcomingClass.objects.all()
    return render(request, 'training_app/home.html', {'classes' : classes})

def course(request):
    return render(request, 'training_app/course.html')
