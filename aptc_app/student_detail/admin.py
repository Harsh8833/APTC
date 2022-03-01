from django.contrib import admin
from student_detail.models import student_detail
from django.contrib.admin.sites import site

class ServiceAdmin(admin.ModelAdmin):
    list_display=('student_name', 'student_rollnumber', 'student_address', 'student_date_of_joining')

admin.site.register(student_detail,ServiceAdmin)
