from django.shortcuts import render

from  django.http import HttpResponse

from . models import Student
from . models import Teacher

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def students(request):
    student = Student.objects.all()
    return render(request, 'students.html',   {"students": student})

def teachers(request):
    teacher = Teacher.objects.all()
    return render(request, 'teachers.html', {"teachers": teacher})

def insert_students(request):
    return render(request, 'insertstud.html')

