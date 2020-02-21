# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-21 09:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('periodOfTime', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('scopeOfCourse', models.CharField(max_length=200)),
                ('notionDiscussed', models.TextField()),
                ('requirementsForEnrolling', models.CharField(max_length=200)),
                ('requiredGear', models.CharField(max_length=200)),
                ('participants', models.CharField(max_length=20)),
                ('trainer', models.CharField(max_length=100)),
                ('participant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
