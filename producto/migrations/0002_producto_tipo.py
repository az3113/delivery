# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.CharField(default=0, max_length=45),
            preserve_default=False,
        ),
    ]
