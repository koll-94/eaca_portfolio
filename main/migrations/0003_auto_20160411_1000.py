# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_document_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctype',
            name='abbr',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doctype',
            name='name',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]