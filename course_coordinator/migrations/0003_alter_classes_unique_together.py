# Generated by Django 3.2.6 on 2021-08-28 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_coordinator', '0002_classes_students_registered'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classes',
            unique_together={('course_code', 'faculty', 'class_time')},
        ),
    ]
