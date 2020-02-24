# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-22 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200222_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='product_ptr',
        ),
        migrations.RemoveField(
            model_name='enrollingrequirements',
            name='course',
        ),
        migrations.RemoveField(
            model_name='gearrequirements',
            name='course',
        ),
        migrations.RemoveField(
            model_name='notions',
            name='course',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='EnrollingRequirements',
        ),
        migrations.DeleteModel(
            name='GearRequirements',
        ),
        migrations.DeleteModel(
            name='Notions',
        ),
    ]