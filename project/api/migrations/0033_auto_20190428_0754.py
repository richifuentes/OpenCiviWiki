# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20190420_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='is_voted_data_updated',
        ),
        migrations.AddField(
            model_name='bill',
            name='vote_data_last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]