# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_manager', '0015_auto_20170519_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacktype',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]
