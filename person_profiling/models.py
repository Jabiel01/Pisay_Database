# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import django_tables2 as tables

sections = (
			('1', '7-Diamond'),
			('2', '7-Gold'),
			('3', '7-Pearl'),
			('4', '8-Dahlia'),
			('5', '8-Kamia'),
			('6', '8-Rosal'),
			('7', '9-Calcium'),
			('8', '9-Lithium'),
			('9', '9-Sodium'),
			('10', '10-Electron'),
			('11', '10-Neutron'),
			('12', '10-Proton'),
			('13', '11-Curie'),
			('14', '11-Darwin'),
			('15', '11-Einstein'),
			('16', '11-Franklin'),
			('17', '11-Newton'),
			('18', '12-Farad'),
			('19', '12-Hertz'),
			('20', '12-Kelvin'),
			('21', '12-Pascal'),
			('22', '12-Tesla'),
	)

infractions = (
		('CC', 'Cutting Class'),
		('T', 'Tardy'),
		('A', 'Absence'),
	)



class Student(models.Model):
	first_name = models.CharField(max_length = 100)
	middle_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	student_number = models.IntegerField()
	section = models.CharField(max_length = 13, choices = sections, default = None)
	balance = models.IntegerField(blank = 0)

	def __unicode__(self):
		return"{} {}".format(self.first_name, self.last_name)


class StudentAttendance(models.Model):
	student = models.ForeignKey(Student)
	time_in = models.DateTimeField(auto_now_add = True)
	time_out = models.DateTimeField(null = True, blank = True)


	class Meta:
		verbose_name_plural = "Student Attendance"

	def __unicode__(self):
		return "{} {}".format(self.student.first_name, self.student.last_name)


class StudentAttendanceTable(tables.Table):
	student = tables.Column()
	time_in = tables.Column()
	time_out = tables.Column()

	class Meta:
		attrs = {'class': "table table-hover"}

class StudentInfractions(models.Model):
	student = models.ForeignKey(Student)
	infraction = models.CharField(max_length = 13, choices = infractions, default = None, null = True, blank = True)
	reason = models.CharField(max_length = 300)
	date_filed = models.DateTimeField(auto_now_add = True)
	date_incurred = models.DateTimeField()
	excused = models.BooleanField(default = False)


	def __unicode__(self):
		return "{}".format(self.student.first_name, self.student.last_name)

	def __unicode__(self):
		return "{}".format(self.student.section)

class StudentInfractionsTable(tables.Table):
	date_filed = tables.Column()
	student = tables.Column()
	infraction = tables.Column()
	date_incurred = tables.Column()
	date_filed = tables.Column()
	excused = tables.Column()

	class Meta:
		attrs = {'class': "table table-hover"}


class Teacher(models.Model):
	first_name = models.CharField(max_length = 100)
	middle_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	teacher_number = models.IntegerField()
	advisory = models.CharField(max_length = 13, choices = sections, null = '')
	balance = models.IntegerField(blank = 0)

	def __unicode__(self):
		return"{} {}".format(self.first_name, self.last_name)


class TeacherAttendance(models.Model):
	teacher = models.ForeignKey(Teacher)
	day_time_in = models.DateTimeField(auto_now_add = True)
	day_time_out = models.DateTimeField(null = True, blank = True)
	afternoon_time_in = models.DateTimeField(null = True, blank = True)
	afternoon_time_out = models.DateTimeField(null = True, blank = True)

	class Meta:
		verbose_name_plural = "Teacher Attendance"

	def __unicode__(self):
		return "{} {}".format(self.teacher.first_name, self.teacher.last_name)

class TeacherInfractions(models.Model):
	teacher = models.ForeignKey(Teacher)
	infraction = models.CharField(max_length = 13, choices = infractions, default = None)
	reason = models.CharField(max_length = 300, default = None)
	date_filed = models.DateTimeField(auto_now_add = True)
	date_incurred = models.DateTimeField()
	excused = models.BooleanField(default = False)

	def __unicode__(self):
		return "{}".format(self.teacher.first_name, self.teacher.last_name)


