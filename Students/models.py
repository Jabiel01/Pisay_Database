# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length = 100)
	middle_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	student_number = models.IntegerField()
	#ID = models.FileField(blank=True, null=True)
	balance = models.IntegerField(blank = 0)

	def __unicode__(self):
		return"{} {}".format(self.first_name, self.last_name)

class Attendance(models.Model):
	student = models.ForeignKey(Student)
	time_in = models.DateTimeField(auto_now_add = True)
	time_out = models.DateTimeField(null = True, blank = True)

	class Meta:
		verbose_name_plural = "Attendance"

	def __unicode__(self):
		return self.student.first_name





# Create your models here.
