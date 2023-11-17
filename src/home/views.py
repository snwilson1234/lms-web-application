from django.shortcuts import render,redirect
from account.models import StudentAccount
from home.models import StudentCourses, StudentCourseGrade,CalendarEvent
from home.forms import CalendarEventForm
from datetime import datetime

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
    context = {}

    scheduled_events = CalendarEvent.objects.filter(owner=request.user)

    calendar_event_form = CalendarEventForm()

    # calendar_events = CalendarEvent.objects.filter(owner=request.user)
    if request.method == "POST":
        calendar_event_form = CalendarEventForm(request.POST)
        if calendar_event_form.is_valid():
            calendar_event = calendar_event_form.save(commit=False)
            calendar_event.owner = str(request.user)
            # input_date_str = calendar_event_form.date
            # input_date_form_str = datetime.strptime(input_date_str, "%a, %b %d, %Y")
            # final_date_str = input_date_form_str.strftime("%Y-%m-%d")
            # calendar_event_form.date = final_date_str
            calendar_event.save()
            print("success event make")

            calendar_event_form.save()
            return redirect('calendar')
        else:
            calendar_event_form = CalendarEventForm()

    context['scheduled_events'] = scheduled_events
    context['calendar_event_form'] = calendar_event_form
    
    
    return render(request, "home/calendar.html", context)