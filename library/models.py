# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import django_tables2 as tables

from person_profiling.models import Student, Teacher


class Book(models.Model):
	book_title = models.CharField(max_length = 100)
	book_number = models.CharField(max_length = 10)
	author = models.CharField(max_length = 100)
	shelf_number = models.CharField(max_length = 20)
	available = models.BooleanField(default = True)
	expected_returned_date = models.DateTimeField(null = True, blank = True)

	def __unicode__(self):
		return"{}".format(self.book_title)


class Borrowee(models.Model):
	student = models.ForeignKey(Student, blank = True, null = True)
	teacher = models.ForeignKey(Teacher, blank = True, null = True)
	book_title = models.ForeignKey(Book)
	date_borrowed = models.DateTimeField(auto_now_add = True)
	expected_returned_date = models.DateTimeField()
	returned = models.BooleanField(default = False)
	fine = models.IntegerField(blank = True, null = True)


class BookTable(tables.Table):
	book_number = tables.Column()
   	book_title = tables.Column()
   	author = tables.Column()
   	shelf_number = tables.Column()
   	available = tables.Column()
   	expected_returned_date = tables.Column()

   	class Meta:
   		attrs = {'class' : "table table-hover"}


class BorroweesTable(tables.Table):
	book_title = tables.Column()
	book_number = tables.Column()
	date_borrowed = tables.Column()
	expected_returned_date = tables.Column()
	returned = tables.Column()
	fine = tables.Column()

	class Meta:
		attrs = {'class' : "table table-hover"}


