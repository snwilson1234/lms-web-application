from django.shortcuts import render
from grades.models import StudentCourseGrade

# Create your views here.

def grades_view(request):
    context = {}

    student_grades = StudentCourseGrade.objects.all()
    context['student_grades'] = student_grades

    return render(request, "grades/grades.html", context)