from django.contrib import admin
from student.models import students_detail
from django.contrib.admin.sites import site

class ServiceAdmin(admin.ModelAdmin):
    list_display=('sclass','board', 'name', 'gender', 'dob', 'fname', 'phone', 'rnum', 'ramt', 'comment', 'doj', 'image1')

admin.site.register(students_detail,ServiceAdmin)
