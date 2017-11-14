# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from Students.models import Student

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'student_number')
    list_filter = ('first_name', 'last_name', 'student_number')
	#list_display = ['student', 'time_in', 'time_out']
	#list_filter = ['time_in']

#admin.site.register(Student)
admin.site.register(Student, AttendanceAdmin)

# Register your models here.
