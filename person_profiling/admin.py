# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from person_profiling.models import Student, StudentAttendance, StudentInfractions, Teacher, TeacherAttendance, TeacherInfractions



class StudentAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'student_number', 'section')
    list_filter = ('first_name', 'last_name', 'student_number', 'section')

class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'time_in', 'time_out')
    list_filter = ('student', 'time_in', 'time_out')

class StudentInfractionsAdmin(admin.ModelAdmin):
    list_display = ('date_filed', 'student', 'date_incurred', 'infraction', 'reason', 'excused')
    list_filter = ('date_filed', 'student', 'date_incurred', 'infraction')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'teacher_number', 'advisory')
    list_filter = ('first_name', 'last_name', 'teacher_number', 'advisory')

class TeacherAttendanceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'teacher', 'day_time_in', 'day_time_out', 'afternoon_time_in', 'afternoon_time_out')
    list_filter = ('teacher', 'day_time_in', 'day_time_out', 'afternoon_time_in', 'afternoon_time_out')

class TeacherInfractionsAdmin(admin.ModelAdmin):
    list_display = ('date_filed', '__unicode__', 'date_incurred', 'infraction', 'reason', 'excused')
    list_filter = ('date_filed', 'date_incurred', 'infraction')

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentAttendance, StudentAttendanceAdmin)
admin.site.register(StudentInfractions, StudentInfractionsAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherAttendance, TeacherAttendanceAdmin)
admin.site.register(TeacherInfractions, TeacherInfractionsAdmin)

# Register your models here.
