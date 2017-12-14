from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from person_profiling.forms import StudentForm
from person_profiling.models import Student, StudentAttendance, StudentInfractions, Teacher, TeacherAttendance, TeacherInfractions

import datetime


def attendance(request):
	context = {}
	message = {}
	if request.method == "POST":
		try:
			student_number = request.POST.get('ID-number')

			try:
				student = get_object_or_404(Student, student_number=student_number)
				attendance = StudentAttendance.objects.filter(student__student_number=student_number).last()
				if not attendance:
					StudentAttendance.objects.create(student=student).save()
					context['message'] = "TIME IN SUCCESSFUL"
				elif attendance.time_out:
					StudentAttendance.objects.create(student=student).save()
					context['message'] = "TIME IN SUCCESSFUL"
				else:
					attendance.time_out = datetime.datetime.now()
					attendance.save()
					context['message'] = "TIME OUT SUCCESSFUL"
				context['attend'] = student
			except:
				pass
			finally:
				try:
					teacher_number = student_number
					try:
						teacher = get_object_or_404(Teacher, teacher_number=teacher_number)
						attendance = TeacherAttendance.objects.filter(teacher__teacher_number=teacher_number).last()
						if not attendance:
							TeacherAttendance.objects.create(teacher=teacher).save()
							context['message'] = "TIME IN"
						elif attendance.time_out:
							TeacherAttendance.objects.create(teacher=teacher).save()
							context['message'] = "TIME IN"
						else:
							attendance.time_out = datetime.datetime.now()
							attendance.save()
							context['message'] = "TIME OUT"	
					except:
						pass
					context['attend'] = teacher
				except:
					pass
		except:
			pass
	return render(request, 'attendance.html', context)


class infractions(View):
	template_name = 'infractions.html'
	context = {}
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'infractions.html', context)

	def post(self, request, *args, **kwargs):
		context = {}

		try:
			student_number = request.POST.get('ID-number')
			try:
				student = get_object_or_404(Student, student_number=student_number)
				StudentInfractions.objects.create(student=student).save()
				context['message'] = "Infraction recorded"
				context['infractions'] = student
			except:
				pass
		except:
			pass

		return render(request, 'infractions.html', context)




