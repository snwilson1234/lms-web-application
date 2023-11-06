from django.shortcuts import render
from account.models import StudentAccount
from home.models import StudentCourses, StudentCourseGrade

# Create your views here.

def home_screen_view(request):
    context = {}

    users = StudentAccount.objects.all()
    context['users'] = users

    user_courses = StudentCourses.objects.filter(username=request.user) 

    print(StudentCourses.objects.filter(username=request.user))
    context['user_courses'] = user_courses
    
    return render(request, "home/home.html", context)

def grades_view(request):
    context = {}

    student_courses = StudentCourses.objects.filter(username=request.user)
    context['student_courses'] = student_courses

    return render(request, "home/grades.html", context)

def courses_view(request):
    context = {}

    student_courses = StudentCourses.objects.filter(username=request.user)
    context['student_courses'] = student_courses

    return render(request, "home/courses.html", context)

def calendar_view(request):
    return render(request, "home/calendar.html")

def webpack_view(request):
    return render(request, "home/hello_webpack.html")