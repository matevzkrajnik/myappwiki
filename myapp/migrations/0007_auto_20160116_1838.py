# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 17:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20160116_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uporabnikprofil',
            name='uporabnik',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profil', to=settings.AUTH_USER_MODEL),
        ),
    ]
