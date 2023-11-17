# Generated by Django 4.2.6 on 2023-11-17 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0029_alter_courses_course_term_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendarevent",
            name="from_time",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="calendarevent",
            name="to_time",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="courses",
            name="course_term",
            field=models.DecimalField(
                choices=[
                    (2221, "Fall 2022-23"),
                    (2231, "Fall 2023-24"),
                    (2227, "Summer 2022-23"),
                    (2224, "Spring 2022-23"),
                    (2234, "Spring 2023-24"),
                    (2237, "Summer 2023-24"),
                ],
                decimal_places=0,
                default=1,
                max_digits=4,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="coursesections",
            name="course_term",
            field=models.DecimalField(
                choices=[
                    (2221, "Fall 2022-23"),
                    (2231, "Fall 2023-24"),
                    (2227, "Summer 2022-23"),
                    (2224, "Spring 2022-23"),
                    (2234, "Spring 2023-24"),
                    (2237, "Summer 2023-24"),
                ],
                decimal_places=0,
                default=1,
                max_digits=4,
                null=True,
            ),
        ),
    ]
