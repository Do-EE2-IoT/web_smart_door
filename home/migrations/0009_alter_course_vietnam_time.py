# Generated by Django 4.2.7 on 2023-12-12 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_course_vietnam_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='vietnam_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 12, 17, 20, 47, 557948)),
        ),
    ]
