from django.db import models
from datetime import datetime
class students_detail(models.Model):
    student_class=models.IntegerField()
    student_board=models.CharField(max_length=10)
    student_name=models.CharField(max_length=50)
    student_gender=models.CharField(max_length=10)
    student_date_of_birth=models.DateField(auto_now_add=True, auto_now=False, blank=True)
    student_father_name=models.CharField(max_length=50)
    student_phone_number=models.IntegerField()
    student_receipt_number=models.IntegerField()
    student_receipt_amount=models.IntegerField()
    student_comments=models.CharField(max_length=100)
    student_date_of_joining=models.DateField(auto_now_add=True, auto_now=False, blank=True)
