from django.shortcuts import render

# Create your views here.

def grades_view(request):
    print(request.headers)
    return render(request, "grades/grades.html", {})