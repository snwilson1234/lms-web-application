from django.shortcuts import render
from sampleclass.models import CourseAnnouncement

# Create your views here.

def sample_class_view(request, course_id):

    context = {}

    announcements = CourseAnnouncement.objects.all()
    context['announcements'] = announcements

    return render(request, "sampleclass/sample_class.html", context)