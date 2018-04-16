from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from canteen.models import Consumable, Purchase, ItemTally, Prices


class ConsumableAdmin(admin.ModelAdmin):
	list_display = ('consumable', 'price')
	list_filter = ('price',)

class PurchaseAdmin(admin.ModelAdmin):
	list_display = ('consumable', 'quantity')
	list_filter = ('consumable',)


class ItemTallyAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'rice_count', 'viand_count', 'meals_count', )

admin.site.register(Consumable, ConsumableAdmin)
admin.site.register(Purchase, PurchaseAdmin)

admin.site.register(ItemTally, ItemTallyAdmin)
admin.site.register(Prices)