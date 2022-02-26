from django.shortcuts import render

# Create your views here.
def allstudents(request):
    return render(request, 'allstudents.html')