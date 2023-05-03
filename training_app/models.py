from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
LEVEL = [
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('A', 'Advance')
]
class Course(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True, default='N/A')
    duration = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    level = models.CharField(max_length=1, choices=LEVEL, default='B')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        db_table = 'Course'



class Instructor(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(limit_value=10)])
    qualification = models.CharField(max_length=50)
    experience_years = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        db_table = 'Instructor'


class UpcomingClass(models.Model):
    title = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    time = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        db_table = 'UpcomingClass'
        verbose_name_plural = 'UpcomingClasses'


    
# class instructor(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     address = models.CharField(max_length=50)
#     experience = models.SmallIntegerField()
#     marital_status = models.BooleanField()
#     email = models.EmailField(unique=True, primary_key=True)
#     p_id = models.OneToOneField(Course, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
