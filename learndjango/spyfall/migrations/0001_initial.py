# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=32)),
                ('created_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=32)),
                ('created_on', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spyfall.Location'),
        ),
        migrations.AddField(
            model_name='card',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spyfall.Role'),
        ),
    ]