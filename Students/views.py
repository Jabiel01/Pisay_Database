from django.contrib import messages
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from Students.forms import StudentForm
from Students.models import Student


class StudentView(View):

	form_class = StudentForm

	def get_context_data(self, *args, **kwargs):
		context = {}
		context['students'] = Student.objects.all()
		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(*args, **kwargs) #students
		form = self.form_class() #form
		context['form'] = form
		return render(request, 'index.html', context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(*args, **kwargs)
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, "Successfully saved!")
			return HttpResponseRedirect(urlresolvers.reverse('Students:students'))
		else:
			context['form'] = form
			return render(request, 'index.html', context)
