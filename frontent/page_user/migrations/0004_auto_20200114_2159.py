# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-14 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_user', '0003_auto_20200114_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_user.UserSecond'),
        ),
    ]