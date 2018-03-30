from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from laboratory.models import Material


class MaterialAdmin(admin.ModelAdmin):
	list_display = ('material', 'quantity')
	list_filter = ('quantity',)

admin.site.register(Material, MaterialAdmin)