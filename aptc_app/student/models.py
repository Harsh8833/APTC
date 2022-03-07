from django.db import models
from datetime import datetime

class_choice = (
    ("1", "11"),
    ("2", "12"),
)
board_choice = (
    ("1", "CBSE"),
    ("2", "BSEB"),
)
gender_choice = (
    ("1", "Male"),
    ("2", "Female"),
)
class students_detail(models.Model):
    sclass=models.CharField(max_length=120, choices=class_choice, default='')
    board=models.CharField(max_length=120, choices=board_choice, default='')
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=120, choices=gender_choice, default='')
    dob=models.DateField(auto_now_add=False, auto_now=False, blank=True)
    fname=models.CharField(max_length=50)
    phone=models.IntegerField()
    rnum=models.IntegerField()
    ramt=models.IntegerField()
    comment=models.CharField(max_length=100)   
    doj=models.DateField(auto_now_add=True, auto_now=False, blank=True)
