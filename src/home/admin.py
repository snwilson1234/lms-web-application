from django.contrib import admin
from home.models import Courses,CourseSections, StudentCourses, StudentCourseGrade

# Register your models here.

class CourseSectionsAdmin(admin.ModelAdmin):
    list_display = ('course_section','course_id','course_instructor')
    search_fields = ('course_section','course_id')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()    

class StudentCoursesAdmin(admin.ModelAdmin):
    list_display = ('username','course_id','course_section_id', 'course_grade', 'course_nickname')
    search_fields = ('username','course_id','course_section_id')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Courses)
admin.site.register(CourseSections, CourseSectionsAdmin)

admin.site.register(StudentCourses, StudentCoursesAdmin)
admin.site.register(StudentCourseGrade)