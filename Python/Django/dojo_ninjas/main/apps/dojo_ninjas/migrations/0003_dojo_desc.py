# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-17 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_ninja'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='DC'),
        ),
    ]
