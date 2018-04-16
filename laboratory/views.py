from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import urlresolvers
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from datetime import datetime, timedelta

from canteen.models import ItemTally 
from laboratory.models import Material, MaterialTable


def MaterialView(request):
	context = {}
	template_name = 'laboratory/materials.html'
	
	materials = Material.objects.all()
	materials = MaterialTable(materials)
	context['materials'] = materials

	return render(request, template_name, context)


