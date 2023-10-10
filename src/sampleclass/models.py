from django.db import models
from home.models import Courses

# Create your models here.
class CourseAnnouncement(models.Model):

    course_announcement_id          = models.AutoField(primary_key=True)
    course_title                    = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True) 
    announcement_title              = models.CharField(max_length=60)
    announcement_text               = models.TextField(max_length=400)
    announcement_date               = models.DateField(auto_now=False, auto_now_add=True)

    #announcement_course = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_id')

    def __str__(self):
        return self.announcement_title
    
    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"