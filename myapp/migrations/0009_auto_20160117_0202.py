# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 01:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20160117_0201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uporabnikprofil',
            old_name='skica_profila',
            new_name='slika_profila',
        ),
    ]
