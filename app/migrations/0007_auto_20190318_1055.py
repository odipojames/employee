# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-18 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190318_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=60),
        ),
    ]