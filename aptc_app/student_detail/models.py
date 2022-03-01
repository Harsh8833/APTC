from django.db import models
class student_detail(models.Model):
    student_name=models.CharField(max_length=50)
    student_rollnumber=models.IntegerField()
    student_address=models.CharField(max_length=50)
    student_date_of_joining=models.DateField()