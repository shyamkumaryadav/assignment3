from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rollNo', 'physics', 'chemistry', 'maths', 'total', 'percentage')
    list_per_page = 20
    list_max_show_all = 100