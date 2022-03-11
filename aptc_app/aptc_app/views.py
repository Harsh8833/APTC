from django.shortcuts import render
from student.models import students_detail

def detail(request):
    return render(request,"admission.html")


def saveEnquiry(request):
    if request.method=="POST":
        sclass=request.POST.get('coursename')
        board=request.POST.get('boardname')
        name=request.POST.get('name')
        gender=request.POST.get('gender1')
        dob=request.POST.get('dob')
        father=request.POST.get('father')
        phone=request.POST.get('phone')
        receipt_no=request.POST.get('receipt_no')
        receipt_amt=request.POST.get('receipt_amt')
        comment=request.POST.get('comment')
        en=students_detail(sclass=sclass, board=board, name=name, gender=gender, dob=dob, fname=father, phone=phone, rnum=receipt_no, ramt=receipt_amt, comment=comment)
        en.save()
    return render(request,"admission.html")


