# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-02 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='access',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='report',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]