# Generated by Django 3.1.7 on 2021-04-05 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210405_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 11, 0, 30, 756048)),
        ),
    ]
