from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from user_account.models import Profile


class ProfileAdmin(admin.ModelAdmin):
	list_display =('user', 'bio', 'location', 'birth_date')


admin.site.register(Profile, ProfileAdmin)