# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-14 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('page_views', models.PositiveIntegerField()),
                ('clicks', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Стать')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip адреса')),
            ],
        ),
        migrations.AddField(
            model_name='statistic',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='page_user.UserSecond'),
        ),
    ]
