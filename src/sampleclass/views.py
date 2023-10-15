from django.shortcuts import render
from sampleclass.models import CourseAnnouncement,CourseModules,ModuleSections
from home.models import Courses,StudentCourses


def sample_class_view(request, course_id):# Pass in course ID (title) clicked

    context = {}

    # Get course object clicked from str passed in above
    course = Courses.objects.get(course_title=course_id)
    course_section = StudentCourses.objects.get(course_id=course)

    context['course'] = course
    context['course_section'] = course_section
    
    # Only show course annoucnements for this course
    announcements = CourseAnnouncement.objects.filter(course_id=course)

    modules       = CourseModules.objects.filter(course_id=course)
    module_sections = ModuleSections.objects.filter(module_id__in=modules)
    
    context['announcements'] = announcements
    context['modules'] = modules
    context['module_sections'] = module_sections

    return render(request, "sampleclass/sample_class.html", context)

def module_view(request):
    return render(request, "sampleclass/module_section.html")