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
    due_date                        = models.DateField(auto_now=False,auto_now_add=False,null=True)

    def __str__(self) -> str:
        return self.assignment_name
    
    class Meta:
        verbose_name = "Course Assignment"
        verbose_name_plural = "Course Assignment"

class AssignmentUploadFile(models.Model):
    file_name               = models.CharField(max_length=60)
    file                    = models.FileField(upload_to='assignments/')
    assignment_id           = models.ForeignKey(CourseAssignments, on_delete=models.CASCADE)
    file_upload_date        = models.DateTimeField(auto_now_add=True)
    uploaded_by             = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.file_name

    class Meta:
        verbose_name = "Uploaded File"
        verbose_name_plural = "Uploaded Files"


class StudentAssignmentGrades(models.Model):
    username            = models.CharField(max_length=60)
    assignment_id       = models.ForeignKey(CourseAssignments, on_delete=models.CASCADE)
    course_id           = models.ForeignKey(Courses, on_delete=models.CASCADE)
    grade               = models.DecimalField(decimal_places=2, max_digits=5)
    submitted_ind       = models.BooleanField(default=False)
    on_time_ind         = models.BooleanField(default=True)
    graded_ind          = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.username} {self.assignment_id} - {self.grade}"

    class Meta:
        verbose_name = "Student Assignment Grade"
        verbose_name_plural = "Student Assignment Grades"