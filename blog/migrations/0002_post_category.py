# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-28 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]