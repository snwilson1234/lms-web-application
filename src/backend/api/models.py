from django.db import models

TERM_CHOICES = {
    ("SP", "Spring"),
    ("FA", "Fall"),
    ("SU", "Summer"),
}

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=60, unique=True, null=True)
    term = models.CharField(max_length=2, choices=TERM_CHOICES)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    
    # need instructor one-to-many (only one instructor per course, instructor can teach many courses)
    # need students many-to-many (course can have many students and students can be enrolled in many courses)
