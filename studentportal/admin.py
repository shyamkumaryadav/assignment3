from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rollNo', 'physics', 'chemistry', 'maths', 'total', 'percentage')