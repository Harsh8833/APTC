from django.contrib import admin
from student.models import students_detail
from django.contrib.admin.sites import site

class ServiceAdmin(admin.ModelAdmin):
    list_display=('student_class','student_board', 'student_name', 'student_gender', 'student_date_of_birth', 'student_father_name',  'student_receipt_number', 'student_receipt_amount', 'student_comments', 'student_date_of_joining')

admin.site.register(students_detail,ServiceAdmin)
