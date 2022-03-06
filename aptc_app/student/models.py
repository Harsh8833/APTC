from django.db import models
from datetime import datetime
class students_detail(models.Model):
    sclass=models.CharField(max_length=120, choices=CONTACT_PREFERENCE, default='')
    board=models.CharField(max_length=120, choices=CONTACT_PREFERENCE, default='')
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=120, choices=CONTACT_PREFERENCE, default='')
    dob=models.DateField(auto_now_add=True, auto_now=False, blank=True)
    fname=models.CharField(max_length=50)
    phone=models.IntegerField()
    rnum=models.IntegerField()
    ramt=models.IntegerField()
    comment=models.CharField(max_length=100)   
    doj=models.DateField(auto_now_add=True, auto_now=False, blank=True)
