# Generated by Django 4.2.7 on 2023-12-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_course_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
    ]
