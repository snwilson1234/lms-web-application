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

    course_title            = models.CharField(max_length=60, unique=True, null=True)
    course_term             = models.DecimalField(max_digits=4, decimal_places=0, choices=TERM_CHOICES, null=True, default=1)
    exam_based              = models.BooleanField(default=True, null=True)
    project_based           = models.BooleanField(default=False, null=True)
    requires_lab            = models.BooleanField(default=False, null=True)


    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

class CourseSections(models.Model):

    course_section          = models.CharField(max_length=60, unique=True, null=True)
    course_id               = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_term             = models.DecimalField(max_digits=4, decimal_places=0, choices=TERM_CHOICES, null=True, default=1)
    course_instructor       = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.course_section

    class Meta:
        verbose_name = "Course Section"
        verbose_name_plural = "Course Sections"

class StudentCourses(models.Model):

    username                    = models.CharField(max_length=30, null=True)
    course_id                   = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_section_id           = models.ForeignKey(CourseSections, on_delete=models.CASCADE)
    course_grade                = models.DecimalField(decimal_places=2, max_digits=5, default=100.00)
    

    def __str__(self):
        return f"{self.username} - {self.course_section_id} - {self.course_id}"

    class Meta:
        verbose_name = "Assigned Course"
        verbose_name_plural = "Student Courses"

class StudentCourseGrade(models.Model):
    course_title        = models.CharField(max_length=60)
    course_grade        = models.DecimalField(decimal_places=2, max_digits=5)
    username            = models.CharField(max_length=60,null=True)


    def __str__(self):
        return self.course_title
    

    class Meta:
        verbose_name = "Course Grade"
        verbose_name_plural = "Course Grades"