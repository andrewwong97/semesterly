# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-05 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_redistrationtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(default=b'')),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='RedistrationToken',
        ),
    ]