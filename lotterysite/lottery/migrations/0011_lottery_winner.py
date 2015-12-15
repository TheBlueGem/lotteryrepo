# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0010_remove_lottery_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lottery.Contestant'),
        ),
    ]
