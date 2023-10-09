from django.contrib import admin
from home.models import Courses,CourseSections, StudentCourses

# Register your models here.

class CourseSectionsAdmin(admin.ModelAdmin):
    list_display = ('course_title','course_section','course_instructor','course_location')
    search_fields = ('course_title','course_section')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()    

class StudentCoursesAdmin(admin.ModelAdmin):
    list_display = ('username','course_title','course_section')
    search_fields = ('username','course_title','course_section')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Courses)
admin.site.register(CourseSections, CourseSectionsAdmin)

admin.site.register(StudentCourses)