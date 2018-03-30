from django import forms

from library.models import Book, Borrowee


class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = ('__all__')
