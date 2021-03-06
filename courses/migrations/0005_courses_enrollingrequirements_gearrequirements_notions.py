# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-22 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_auto_20200222_1025'),
        ('courses', '0004_auto_20200222_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
                ('description', models.TextField()),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('periodOfTime', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('participants', models.CharField(max_length=20)),
                ('totalParticipants', models.IntegerField(default=0)),
                ('video_url', models.CharField(blank=True, max_length=200, null=True)),
                ('trainer', models.CharField(max_length=100)),
            ],
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='EnrollingRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirementsForEnrolling', models.CharField(blank=True, max_length=200, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='GearRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requiredGear', models.CharField(blank=True, max_length=200, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Notions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notionDiscussed', models.CharField(blank=True, max_length=100, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
            ],
        ),
    ]
