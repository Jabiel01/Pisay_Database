from __future__ import unicode_literals
from django.db import models

import django_tables2 as tables

from person_profiling.models import Student, Teacher

class Consumable(models.Model):
	consumable = models.CharField(max_length = 30)
	price = models.FloatField()
	quantity = models.IntegerField(default = 0, blank = True)

	def __unicode__(self):
		return "{}".format(self.consumable)


class ConsumableTable(tables.Table):
	consumable = tables.Column()
	price = tables.Column()
	quantity = tables.Column()

	class Meta:
		attrs = {'class' : "table table-hover"}


class Purchase(models.Model):
	Student = models.ForeignKey(Student, blank = True, null = True)
	Teacher = models.ForeignKey(Teacher, blank = True, null = True)
	consumable = models.ForeignKey(Consumable)
	quantity = models.IntegerField(default = 0, blank = True)

