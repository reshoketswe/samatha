# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-22 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200222_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='mobile_uploads'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
