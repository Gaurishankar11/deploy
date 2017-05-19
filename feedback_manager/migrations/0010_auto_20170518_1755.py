# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_manager', '0009_auto_20170518_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='feedbackappointmentmap',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback_manager.NewAppointment'),
        ),
    ]
