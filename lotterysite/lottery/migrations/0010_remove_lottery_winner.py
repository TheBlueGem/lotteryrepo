# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0009_lottery_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottery',
            name='winner',
        ),
    ]