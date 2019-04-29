from django.contrib import admin
from courses.models import Course
from courses.models import Review


admin.site.register(Course)
admin.site.register(Review)
