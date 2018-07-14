# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 11:30
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20180505_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='comment',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='questioncomment',
            name='comment',
            field=tinymce.models.HTMLField(),
        ),
    ]