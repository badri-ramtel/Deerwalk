from django.shortcuts import render, redirect
from training_app.models import UpcomingClass, Courses, delete

# Create your views here.
def home(request):
    classes = UpcomingClass.objects.all()
    return render(request, 'training_app/home.html', {'classes' : classes})

def courses(request):
    courses = Courses.objects.all() # all().order_by('-price', 'title')
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
        Courses.objects.create(title = title, description = desc, duration = duration, price = price, level = level)

        # return render(request, 'training_app/courses.html') --> it just show the page of other html in its own page
        return redirect('training-courses')
    
def delete(request, id):
    course = Courses.objects.get(id=id)
    course.delete()

    return redirect('training-courses')

def edit(request, id):
    if request.method == 'GET':
        course = Courses.objects.get(id=id)
        return render(request, 'training_app/edit.html', {'course' : course})
    else:
        # title = request.POST['title']
        # desc = request.POST['description']
        # duration = request.POST['duration']
        # price = request.POST['price']
        # level = request.POST['level']

        course = Courses.objects.get(id=id)
        course.title = request.POST['title']
        course.description = request.POST['description']
        course.duration = request.POST['duration']
        course.price = request.POST['price']
        course.level = request.POST['level']

        course.save()

        return redirect('training-courses')
