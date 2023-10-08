from django.db import models

# Create your models here.

class StudentCourseGrade(models.Model):
    course_title = models.CharField(max_length=60)
    course_grade = models.DecimalField(decimal_places=2, max_digits=5)


    def __str__(self):
        return self.course_title
    

    class Meta:
        verbose_name = "Course Grade"
        verbose_name_plural = "Course Grades"