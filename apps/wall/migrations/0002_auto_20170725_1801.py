# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-25 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friendedBy',
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.User'),
            preserve_default=False,
        ),
    ]
