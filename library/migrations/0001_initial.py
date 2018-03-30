# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person_profiling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_number', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=100)),
                ('shelf_number', models.CharField(max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('expected_returned_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_borrowed', models.DateTimeField(auto_now_add=True)),
                ('expected_returned_date', models.DateTimeField()),
                ('returned', models.BooleanField(default=False)),
                ('fine', models.IntegerField(blank=True, null=True)),
                ('book_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person_profiling.Student')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person_profiling.Teacher')),
            ],
        ),
    ]
