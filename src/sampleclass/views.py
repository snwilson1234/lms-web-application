from django.shortcuts import render
from sampleclass.models import Announcement

# Create your views here.

def sample_class_view(request):

    context = {}

    announcements = Announcement.objects.all()
    context['announcements'] = announcements

    return render(request, "sampleclass/sample_class.html", context)