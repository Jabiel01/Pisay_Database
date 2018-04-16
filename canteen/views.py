from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import urlresolvers
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from datetime import datetime, timedelta

from canteen.models import Consumable, ConsumableTable, ItemTally
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


def account_balance(request):
    if request.method == "POST":
        Choice = request.POST.get("s_use")
        if int(Choice)==1:
            x=1
        else:
            x=2
    
        if 'q' in request.POST and request.POST['q']:
            q = request.POST['q']
            if x==1:
                students = Student.objects.filter(student_number=q).values()
            elif x==2:
                students = Student.objects.filter(first_name__icontains=q).values()
          
            item_tallies = list()
            for student in students:
                tallies = ItemTally.objects.filter(
                    student__student_number=student.get('student_number'))

            return render(request, 'canteen/canteen_results.html', {'students': tallies, 
                'total': tallies[0].student.balance, 
                'query': q})
        else:
            return HttpResponse('Please submit a search term')
    else: 
        return render (request, 'canteen/canteen_results.html', {})
  
def canteen_in(request):
  return render(request, 'canteen/order.html')  

def canteen(request):
    sid = request.GET['sid']
    context = {}
    try:
        student = Student.objects.get(student_number=sid)
        ItemTally.objects.create(student=student).save()
        context['sid']=sid
    except:
        messages.error(request, "Transaction Failed")
        return render(request, 'canteen/order.html', context)
    return render(request, 'canteen/order2.html', context)
def order(request):

    context = {}
    if request.method == "POST":
        sid = request.POST.get('sid')
        v_rice = request.POST.get("rice", 0)
        v_viand = request.POST.get("viand", 0)
        v_meal = request.POST.get("meal", 0)
        new = ItemTally.objects.filter(student__student_number=sid).last()
        ore = new.rice_count
        new.rice_count = ore + int(v_rice)
        ove = new.viand_count
        new.viand_count = ove + int(v_viand)
        ome = new.meals_count
        new.meals_count = ome + int(v_meal)
        new.save()
        messages.success(request, 'Transaction Complete')
    return render(request, 'canteen/order.html', context)
