# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandadas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandada',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
