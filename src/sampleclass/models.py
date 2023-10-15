from django.db import models
from home.models import Courses

# Announcements
class CourseAnnouncement(models.Model):

    course_id                       = models.ForeignKey(Courses, on_delete=models.CASCADE) 
    announcement_title              = models.CharField(max_length=60)
    announcement_text               = models.TextField(max_length=400)
    announcement_date               = models.DateField(auto_now=False, auto_now_add=True)

    #announcement_course = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_id')

    def __str__(self):
        return self.announcement_title
    
    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"


# Modules

class CourseModules(models.Model):

    module_name                     = models.CharField(max_length=60)
    course_id                       = models.ForeignKey(Courses, on_delete=models.CASCADE) 
    order_sequence                  = models.DecimalField(max_digits=3,decimal_places=0)
    active_ind                      = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.module_name
    
    class Meta:
        verbose_name = "Course Module"
        verbose_name_plural = "Course Modules"

class ModuleSections(models.Model):

    module_section_name             = models.CharField(max_length=60)
    module_id                       = models.ForeignKey(CourseModules, on_delete=models.CASCADE)
    order_sequence                  = models.DecimalField(max_digits=3,decimal_places=0)
    active_ind                      = models.BooleanField(default=True)
    clickable_ind                   = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.module_section_name} - {self.module_id}"
    
    class Meta:
        verbose_name = "Module Section"
        verbose_name_plural = "Module Sections"


# Assignments

class CourseAssignments(models.Model):

    assignment_name                 = models.CharField(max_length=60)
    course_id                       = models.ForeignKey(Courses, on_delete=models.CASCADE) 
    order_sequence                  = models.DecimalField(max_digits=3,decimal_places=0)
    active_ind                      = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.assignment_name
    
    class Meta:
        verbose_name = "Course Assignment"
        verbose_name_plural = "Course Assignment"