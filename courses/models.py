from django.db import models
from students.models import Student
from instructors.models import Instructor

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Enrollments')
    instructor = models.ForeignKey(
        Instructor, 
        on_delete=models.SET_NULL,
        null=True, 
        related_name='courses'
    )

    def __str__(self):
        return self.name
        
class Enrollments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    enrollment_date = models.DateField(auto_now_add=True)