from django.contrib import admin
from sampleclass.models import CourseAnnouncement,CourseModules,ModuleSections, CourseAssignments, AssignmentFile

# Register your models here.

class AssignmentFileAdmin(admin.ModelAdmin):
    list_display = ('file_name','assignment_id','file')
    search_fields = ('file_name','assignment_id','file')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()   

admin.site.register(CourseAnnouncement)
admin.site.register(CourseModules)
admin.site.register(ModuleSections)
admin.site.register(CourseAssignments)
admin.site.register(AssignmentFile, AssignmentFileAdmin)