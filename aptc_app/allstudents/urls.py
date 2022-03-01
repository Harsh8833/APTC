from django.urls import path
from . import views


urlpatterns = [
    path('', views.allstudents , name= 'allstudents')
]
