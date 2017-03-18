# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_api', '0002_remove_samplemodel_apigroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=128)),
                ('url', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='SampleModel',
        ),
    ]
