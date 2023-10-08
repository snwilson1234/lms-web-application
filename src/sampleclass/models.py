from django.db import models

# Create your models here.
class Announcement(models.Model):
    announcement_title = models.CharField(max_length=60)
    announcement_text = models.TextField(max_length=400)
    announcement_date = models.DateField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.announcement_title
    

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"