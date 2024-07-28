# Generated by Django 5.0.7 on 2024-07-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, null=True, unique=True)),
                ('term', models.CharField(choices=[('SP', 'Spring'), ('SU', 'Summer'), ('FA', 'Fall')], max_length=2)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
