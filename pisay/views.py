from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View


def homeview(request):
	return render(request, 'static/base.html')

def aboutview(request):
	return render(request, 'static/pages/About.html')