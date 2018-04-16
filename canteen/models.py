from __future__ import unicode_literals
from django.db import models

import django_tables2 as tables

from person_profiling.models import Student, Teacher


optional = {
	'blank': True,
	'null': True
}

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



class Prices(models.Model):
	rice_price = models.IntegerField(default=0, **optional)
	viand_price = models.IntegerField(default=0, **optional)
	meals_price = models.IntegerField(default=0, **optional)

	def __unicode__(self):
		return "RICE: {} VIAND:{} MEALS:{}".format(
			self.rice_price,
			self.viand_price,
			self.meals_price)

	class Meta:
		verbose_name_plural = "Prices"


class ItemTally(models.Model): 
	rice_count = models.IntegerField(default=0, **optional) 
	viand_count = models.IntegerField(default=0, **optional) 
	meals_count = models.IntegerField(default=0, **optional) 
	student = models.ForeignKey(Student)
	total = models.IntegerField(**optional)

	def calculate(self):
		price = Prices.objects.all().last()
		total_rice_amount = price.rice_price * self.rice_count
		total_viand_amount = price.viand_price * self.viand_count
		total_meals_amount = price.meals_price * self.meals_count
		total = total_rice_amount + total_viand_amount + total_meals_amount
		return total

	def save(self, *args, **kwargs):
		balance = self.student.balance - self.calculate()
		self.total = self.calculate()
		self.student.balance = balance
		self.student.save()
		super(ItemTally, self).save(*args, **kwargs)		
    
	def __unicode__(self):
		return "{}".format(self.student)

	class Meta:
		verbose_name_plural = "Item Tallies"