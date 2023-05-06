from django.contrib import admin
# from training_app.models import UpcomingClass, Instructor, Courses
from training_app.models import *

# Register your models here.
admin.site.register(UpcomingClass)
admin.site.register(Instructor)
admin.site.register(Courses)
