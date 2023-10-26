from django.shortcuts import render
from sampleclass.models import CourseAnnouncement,CourseModules,ModuleSections, CourseAssignments, AssignmentUploadFile
from sampleclass.forms import AssignmentUploadForm
from home.models import Courses,StudentCourses
from django.http import HttpResponseRedirect

from sampleclass.assignment_upload import handle_uploaded_file


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

def assignment_detail_view(request, course_id, assignment_id):
    context = {}
    
    # Get the course object for the given course_id
    course = Courses.objects.get(course_title=course_id)

    # Query the assignments related to the course
    assignment = CourseAssignments.objects.get(assignment_name=assignment_id)
    form = AssignmentUploadForm()

    CourseAssignments.objects.check

    # Get uploaded files
    files = AssignmentUploadFile.objects.filter(assignment_id=assignment)

    #file uploading
    if request.method == "POST":
        form = AssignmentUploadForm(request.POST, request.FILES)

        if form.is_valid():
            assignment_upload = form.save(commit=False)
            assignment_upload.assignment_id = assignment
            assignment_upload.file_name = str(assignment_upload.file).replace(' ','_')
            assignment_upload.save()

            form.save()
        else:
            form = AssignmentUploadForm()
    
    context['course'] = course
    context['assignment'] = assignment
    context['upload_form'] = form
    context['uploaded_files'] = files
    
    return render(request, "sampleclass/assignment_detail.html", context)


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

def module_detail_view(request, course_id, module_name, module_section_name):
    context = {}
    
    # Get the course object for the given course_id
    course = Courses.objects.get(course_title=course_id)
    
    # Query the assignments related to the course
    module       = CourseModules.objects.get(module_name=module_name)
    module_section = ModuleSections.objects.get(module_section_name=module_section_name)
    
    context['course'] = course
    context['module'] = module
    context['module_section'] = module_section
    
    return render(request, "sampleclass/module_detail.html", context)