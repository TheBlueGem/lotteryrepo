# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0008_lottery_lot_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='name',
            field=models.CharField(default='Vrije Loterij', max_length=30),
            preserve_default=False,
        ),
    ]
