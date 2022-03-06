from django.shortcuts import render
from student.models import students_detail

def detail(request):
    return render(request,"admission.html")


def saveEnquiry(request):
    if request.method=="POST":
        clas=request.POST.get('class')
        board=request.POST.get('board')
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        father=request.POST.get('father')
        phone=request.POST.get('phone')
        receipt_no=request.POST.get('receipt_no')
        receipt_amt=request.POST.get('receipt_amt')
        comment=request.POST.get('comment')
        en=students_detail(student_class=clas, student_board=board, student_name=name, student_gender=gender, student_date_of_birth=dob, student_father_name=father, student_phone_number=phone, student_receipt_number=receipt_no, student_receipt_amount=receipt_amt, student_comments=comment)
        en.save()
    return render(request,"admission.html")


