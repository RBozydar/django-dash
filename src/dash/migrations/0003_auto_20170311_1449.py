# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 20:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20170126_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardplugin',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='dashboardplugin',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='dashboardsettings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
