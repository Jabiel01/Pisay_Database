# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

#from user_account.forms import SignUpForm
from person_profiling.forms import StudentForm, TeacherForm
from person_profiling.models import Student, Teacher

def newstudentuserView(request):
	context = {}
	template_name = 'new_user/student_signup.html'
	form = StudentForm(request.POST)
	context['form'] = form	

	if request.method == 'POST':
		if form.is_valid():
			user = form.save()
			username = get_object_or_404(Student, user=user)
			username.first_name = form.cleaned_data.get('first_name')
			username.middle_name = form.cleaned_data.get('middle_name')
			username.last_name = form.cleaned_data.get('last_name')
			username.student_number = form.cleaned_data.get('student_number')
			username.section = form.cleaned_data.get('section')
			username.save()
			context['user'] = user
			context['message'] = 'student user account has been created.'
	
	else:
		context['form'] = form

	return render(request, template_name, context)

def newteacheruserView(request):
	context = {}
	template_name = 'new_user/teacher_signup.html'
	form = TeacherForm(request.POST)
	context['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			user = form.save()
			username = get_object_or_404(Teacher, user=user)
			username.first_name = form.cleaned_data.get('first_name')
			username.middle_name = form.cleaned_data.get('middle_name')
			username.last_name = form.cleaned_data.get('last_name')
			username.teacher_number = form.cleaned_data.get('teacher_number')
			username.save()

			context['user'] = user
			context['message'] = 'teacher user account has been created'

	else:
		context['form'] = form

	return render(request, template_name, context)
