from django.shortcuts import render

# Create your views here.
def home(request):
    a = ['ram', 'shyam', 'hari']
    return render(request, 'college_app/home.html', {'names' : a})