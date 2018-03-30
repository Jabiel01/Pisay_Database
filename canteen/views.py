from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import urlresolvers
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from datetime import datetime, timedelta

from canteen.models import Consumable, ConsumableTable
from canteen.forms import PurchaseForm
from person_profiling.models import Student, Teacher


def ConsumableView(request):
	context = {}
	template_name = "canteen/consumable_list.html"

	consumables = ConsumableTable(Consumable.objects.all())
	context['consumables'] = consumables

	return render(request, template_name, context)

def PurchaseView(request):
	context = {}
	template_name = "canteen/purchase.html"

	consumables = ConsumableTable(Consumable.objects.all())
	context['consumables'] = consumables

	return render(request, template_name, context)

"""	if request.POST:
		form = PurchaseForm(request.POST)
		if form.is_valid():
			form.save()
			context['message'] = "Form saved"
		else:
			context['message'] = "Form is not valid"
	else:
		form = PurchaseForm()


	context['form'] = form"""


def ViewBalance(request):
	context = {}
	template_name = "canteen/balance.html"

	if request.method == "POST":
		try:
			ID_number = request.POST.get('ID-number')
			try:
				student = get_object_or_404(Student, student_number = ID_number)
				context['user_exists'] = student

				balance = student.balance
				context['balance'] = balance
			except:
				teacher = get_object_or_404(Teacher, teacher_number = ID_number)
				context['user_exists'] = teacher

				balance = teacher.balance
				context['balance'] = balance
		except:
			context['user_exists'] = "No User Found"

	return render(request, template_name, context)

def ReloadBalance(request):
	context = {}
	template_name = "canteen/reload.html"

	if request.method == "POST":
		try:
			ID_number = request.POST.get('ID-number')
			try:
				load = request.POST.get('load')
				try:
					student = get_object_or_404(Student, student_number = ID_number)
					context['user_exists'] = student

					balance = student.balance+int(load)
					student.balance = balance
					student.save()
					context['load'] = load
					context['balance'] = balance
				except:
					teacher = get_object_or_404(Teacher, teacher_number = ID_number)
					context['user_exists'] = teacher

					balance = teacher.balance+load
					teacher.balance = balance
					teacher.save()
					context['load'] = load
					context['balance'] = balance
			except:
				context['load'] = "No load Entered"
		except:
			context['user_exists'] = "No User Found"

	return render(request, template_name, context)


