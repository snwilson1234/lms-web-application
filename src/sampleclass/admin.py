from django.contrib import admin
from sampleclass.models import CourseAnnouncement,CourseModules,ModuleSections, CourseAssignments, AssignmentUploadFile, StudentAssignmentGrades

# Register your models here.

class AssignmentFileAdmin(admin.ModelAdmin):
    list_display = ('file_name','assignment_id','file','file_upload_date', 'uploaded_by')
    search_fields = ('file_name','assignment_id','file','file_upload_date', 'uploaded_by')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()   

admin.site.register(CourseAnnouncement)
admin.site.register(CourseModules)
admin.site.register(ModuleSections)
admin.site.register(CourseAssignments)
admin.site.register(AssignmentUploadFile, AssignmentFileAdmin)
admin.site.register(StudentAssignmentGrades)