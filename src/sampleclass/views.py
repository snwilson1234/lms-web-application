from django.shortcuts import render
from sampleclass.models import CourseAnnouncement,CourseModules,ModuleSections, CourseAssignments
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

    assignments   = CourseAssignments.objects.filter(course_id=course)
    
    context['announcements'] = announcements
    context['modules'] = modules
    context['module_sections'] = module_sections
    context['assignments'] = assignments

    return render(request, "sampleclass/sample_class.html", context)

def assignments_view(request, course_id):
    context = {}
    
    # Get the course object for the given course_id
    course = Courses.objects.get(course_title=course_id)
    
    # Query the assignments related to the course
    assignments = CourseAssignments.objects.filter(course_id=course)
    
    context['course'] = course
    context['assignments'] = assignments
    
    return render(request, "sampleclass/assignments.html", context)

def announcements_view(request, course_id):# Pass in course ID (title) clicked

    context = {}

    # Get course object clicked from str passed in above
    course = Courses.objects.get(course_title=course_id)

    context['course'] = course
    
    # Only show course annoucnements for this course
    announcements = CourseAnnouncement.objects.filter(course_id=course)

    context['announcements'] = announcements

    return render(request, "sampleclass/announcements.html", context)


def modules_view(request, course_id):# Pass in course ID (title) clicked

    context = {}

    # Get course object clicked from str passed in above
    course = Courses.objects.get(course_title=course_id)
    course_section = StudentCourses.objects.get(course_id=course)

    context['course'] = course
    context['course_section'] = course_section

    modules       = CourseModules.objects.filter(course_id=course)
    module_sections = ModuleSections.objects.filter(module_id__in=modules)
    
    context['modules'] = modules
    context['module_sections'] = module_sections

    return render(request, "sampleclass/modules.html", context)