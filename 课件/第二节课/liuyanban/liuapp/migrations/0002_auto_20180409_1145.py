# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 11:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liuapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liuyanmodels',
            old_name='information',
            new_name='message',
        ),
    ]
