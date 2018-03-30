from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import urlresolvers
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from datetime import datetime, timedelta

from library.models import Book, BookTable, Borrowee, BorroweesTable

from person_profiling.models import Student, Teacher


def Borrow_Book(request):
	context = {}
	template_name = 'library/borrow_book.html'

	if request.method == "POST":
		if 'borrow_btn' in request.POST:
			try:
				student_number = request.POST.get('ID-number')
				try:
					student = get_object_or_404(Student, student_number=student_number)
					context['user_exists'] = student
					try:
						book_number = request.POST.get('book-number')
						try:
							book = get_object_or_404(Book, book_number=book_number)
							if book.available == True:
								Borrowee.objects.create(student=student,book_title=book,expected_returned_date=datetime.now() + timedelta (days = 7))
								book.available = False
								book.expected_returned_date = datetime.now() + timedelta (days = 7)
								book.save()
								context['book'] = book
							else:
								context['book'] = "Book hasn't been returned yet"
						except:
							context['book'] = "Incorrect Book Number"
					except:
						context['book'] = "No book Found"
				except:
					teacher_number = request.POST.get('ID-number')
					try:
						teacher = get_object_or_404(Teacher, teacher_number=teacher_number)
						context['user_exists'] = teacher
						try:
							book_number = request.POST.get('book-number')
							try:
								book = get_object_or_404(Book, book_number=book_number)
								Borrowee.objects.create(Teacher=teacher,book_title=book,expected_returned_date=datetime.now() + timedelta (days = 7))
								book.available = False
								book.expected_returned_date = datetime.now() + timedelta (days = 7)
								book.save()
								context['book'] = book
							except:
								context['book'] = "Incorrect Book Number"
						except:
							context['book'] = "No book Found"
					except:
						context['user_exists'] = "No User Found"
			except:
				context['user_exists'] = "No User Found"

		elif 'book-number-return' in request.POST:
			books = Book.objects.all()
			borrowed_books = Borrowee.objects.all()
			book_number = request.POST.get('book-number-return')
			try:
				book = get_object_or_404(Book, book_number=book_number)
				borrowed_books = borrowed_books.filter(book_title=book).last()
				if book.available == False:
					borrowed_books.returned = True
					borrowed_books.save()
					book.expected_returned_date = datetime.now()
					book.available = True
					book.save()
					context['returned'] = "The book has been returned"
				else:
					context['returned'] = "This book was not borrowed in the first place"
			except:
				context['returned'] = "No such book"
	

	return render(request, template_name, context)


def Personal_Library_Card(request):
	context = {}
	Borrowees = Borrowee.objects.all()


	template_name = 'library/personal_library_card.html'


	if request.method == "POST":
		try:
			ID_number = request.POST.get('ID-number')
			try:
				student = get_object_or_404(Student, student_number = ID_number)
				Borrowees = Borrowees.filter(student__student_number = ID_number)
				Borrowees = BorroweesTable(Borrowees)
				Borrowees.paginate(page=request.GET.get('page',1), per_page=20)
				context['borrowed_log'] = Borrowees
				context['user_exists'] = student

			except:
				try:
					teacher = get_object_or_404(Teacher, teacher_number=ID_number)
					Borrowees = Borrowees.filter(teacher__teacher_number = ID_number)
					Borrowees = BorroweesTable(Borrowees)
					Borrowees.paginate(page=request.GET.get('page',1), per_page=20)
					context['borrowed_log'] = Borrowees
					context['user_exists'] = teacher
					
				except:
					context['borrowed_log'] = "No User Found"	
		except:
			context['borrowed_log'] = "User does not exist"

	return render(request, template_name, context)


def Search_Book(request):
	books = Book.objects.all()
	context = {}
	template_name = 'library/search_book.html'

	booked = request.POST.get('book')
	if booked:
		book = books.filter(Q(book_title__icontains = booked) | Q(book_number__icontains = booked) | Q(author__contains = booked))
		book_table = BookTable(book)
		book_table.paginate(page=request.GET.get('page', 1), per_page=25)
		context['book'] = book
		context['book_table'] = book_table


	return render(request, template_name, context)





