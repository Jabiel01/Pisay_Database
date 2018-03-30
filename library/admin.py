# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from library.models import Book, Borrowee


class BookAdmin(admin.ModelAdmin):
	list_display  = ('book_title', 'author', 'book_number', 'shelf_number', 'available', 'expected_returned_date')
	list_filter = ('book_title', 'author', 'book_number', 'shelf_number')

class BorroweeAdmin(admin.ModelAdmin):
	list_display = ('date_borrowed','student','teacher','book_title', 'expected_returned_date','returned','fine')
	list_filter = ('date_borrowed','student','teacher','book_title')

admin.site.register(Book, BookAdmin)
admin.site.register(Borrowee, BorroweeAdmin)