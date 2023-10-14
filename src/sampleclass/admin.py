from django.contrib import admin
from sampleclass.models import CourseAnnouncement,CourseModules,ModuleSections

# Register your models here.

admin.site.register(CourseAnnouncement)
admin.site.register(CourseModules)
admin.site.register(ModuleSections)
