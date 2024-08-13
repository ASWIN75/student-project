from django.shortcuts import render, redirect
from StudentApp.models import Student

def show_student(request):
    return render(request, "student.html")

def add_student(request):
    if request.method == 'POST':
        sname = request.POST['student_name']
        adr = request.POST['student_address']
        age = request.POST['student_age']
        email = request.POST['student_email']
        jdate = request.POST['joining_date']
        qual = request.POST['qualification']
        gend = request.POST['gender']
        number = request.POST['mobile_num']
        std = Student(student_name=sname, address=adr, age=age, email=email, joining_date=jdate, qualification=qual, gender=gend, mobile_number=number)
        std.save()
        return redirect('show_student_details')

def show_student_details(request):
    students = Student.objects.all()
    return render(request, "show_student.html", {'std': students})

def editpage(request, pk):
    std = Student.objects.get(id=pk)
    return render(request, 'edit.html', {'student': std})

def edit_student_details(request, pk):
    if request.method == 'POST':
        std = Student.objects.get(id=pk)
        std.student_name = request.POST.get('student_name')
        std.address = request.POST.get('student_address')
        std.age = request.POST.get('student_age')
        std.email = request.POST.get('student_email')
        std.joining_date = request.POST.get('joining_date')
        std.qualification = request.POST.get('qualification')
        std.gender = request.POST.get('gender')
        std.mobile_number = request.POST.get('mobile_num')
        std.save()
        return redirect('show_student_details')
    return render(request, 'edit.html')

def deletepage(request, pk):
    std = Student.objects.get(id=pk)
    std.delete()
    return redirect('show_student_details')

def student_details(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'student_details.html', {'student': student})  # New view function
