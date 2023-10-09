from django.db import models

TERM_CHOICES = {
        (2221, 'Fall 2022-23'),
        (2224, 'Spring 2022-23'),
        (2227, 'Summer 2022-23'),
        (2231, 'Fall 2023-24'),
        (2234, 'Spring 2023-24'),
        (2237, 'Summer 2023-24'),
    }

class Courses(models.Model):

    course_title            = models.CharField(max_length=60, unique=True)
    course_term             = models.DecimalField(max_digits=4, decimal_places=0, choices=TERM_CHOICES)
    # course_instructor       = models.CharField(max_length=100)
    # course_location         = models.CharField(max_length=100)
    exam_based              = models.BooleanField(default=True)
    project_based           = models.BooleanField(default=False)
    requires_lab            = models.BooleanField(default=False)

    # course_open_seats            = models.DecimalField(max_digits=3)

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

class CourseSections(models.Model):

    course_section          = models.CharField(max_length=60, unique=True)
    course_title            = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_instructor       = models.CharField(max_length=100)
    course_location         = models.CharField(max_length=100)
    
    course_open_seats       = models.DecimalField(max_digits=3, decimal_places=0)
    course_taken_seats      = models.DecimalField(max_digits=3, decimal_places=0)
    course_waitlist         = models.DecimalField(max_digits=2, decimal_places=0)


    def __str__(self):
        return self.course_section

    class Meta:
        verbose_name = "Course Section"
        verbose_name_plural = "Course Sections"

class StudentCourses(models.Model):

    username                = models.CharField(max_length=30, unique=True)
    course_section          = models.CharField(max_length=60, unique=True)
    course_title            = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} - {self.course_section} - {self.course_title}"

    class Meta:
        verbose_name = "Assigned Course"
        verbose_name_plural = "Student Courses"