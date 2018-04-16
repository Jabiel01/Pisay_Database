from __future__ import unicode_literals
from django.db import models

import django_tables2 as tables

from person_profiling.models import Student, Teacher


class Material(models.Model):
	material = models.CharField(max_length = 30)
	quantity = models.IntegerField(default=0)


class MaterialTable(tables.Table):
	material = tables.Column()
	quantity = tables.Column()

	class Meta:
		attrs = {'class' : "table table-hover"}

