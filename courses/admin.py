from django.contrib import admin

from courses.models import Course, Enrollments

admin.site.register(Course)
admin.site.register(Enrollments)
