# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_manager', '0003_auto_20170517_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday')], max_length=1),
        ),
    ]
