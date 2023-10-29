from .models import StudentCourses

def student_course_renderer(request):
    return {
        'student_courses': StudentCourses.objects.filter(username=request.user)
    }