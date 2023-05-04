from django.shortcuts import render, redirect
from training_app.models import UpcomingClass, Course

# Create your views here.
def home(request):
    classes = UpcomingClass.objects.all()
    return render(request, 'training_app/home.html', {'classes' : classes})

def courses(request):
    courses = Course.objects.filter(title__iexact = 'Java') # all().order_by('-price', 'title')
    return render(request, 'training_app/courses.html', {'courses' : courses})

def add_course(request):
    # print('*******')
    # print(request.method)
    # print(request.POST)
    if request.method == 'GET':
        return render(request, 'training_app/add_course.html')
    
    elif request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['description']
        duration = request.POST['duration']
        price = request.POST['price']
        level = request.POST['level']

        # c = Course(title = title, description = desc, duration = duration, price = price, level = level)
        # c.save()
        Course.objects.create(title = title, description = desc, duration = duration, price = price, level = level)

        # return render(request, 'training_app/courses.html') --> it just show the page of other html in its own page
        return redirect('training-course')