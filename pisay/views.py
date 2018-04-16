from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View


def aboutview(request):
	return render(request, 'static/stock/about.html')

def admissionview(request):
	return render(request, 'static/stock/admission.html')

def homeview(request):
	return render(request, 'static/stock/home.html')

