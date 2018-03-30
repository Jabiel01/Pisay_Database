from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import urlresolvers
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from person_profiling.forms import StudentForm, StudentInfractionsForm
from person_profiling.models import Student, StudentAttendance, StudentAttendanceTable, StudentInfractions, StudentInfractionsTable, Teacher, TeacherAttendance, TeacherInfractions

import datetime


def attendance(request):
	context = {}
	message = {}
	template_name = 'attendance/attendance.html'

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
							context ['message'] = "DAY TIME IN"
						elif attendance.afternoon_time_out:
							TeacherAttendance.objects.create(teacher=teacher).save()
							context ['message'] = "DAY TIME IN"						
						elif attendance.afternoon_time_in:
							attendance.afternoon_time_out = datetime.datetime.now()
							attendance.save()
							context ['message'] = "AFTERNOON TIME OUT"
						elif attendance.afternoon_time_in:
							attendance.afternoon_time_out = datetime.datetime.now()
							attendance.save()
							context ['message'] = "AFTERNOON TIME OUT"
						elif attendance.day_time_out:
							attendance.afternoon_time_in = datetime.datetime.now()
							attendance.save()
							context ['message'] = "AFTERNOON TIME IN" 
						elif attendance.day_time_in:
							attendance.day_time_out = datetime.datetime.now()
							attendance.save()
							context ['message'] = "DAY TIME OUT"	
					except:
						pass
					context['attend'] = teacher
				except:
					pass
		except:
			pass
	return render(request, template_name, context)


def infractions(request):
	context = {}
	template_name = 'attendance/infractions.html' 
	form = StudentInfractionsForm(request.POST or None)
	context['form'] = form

	if request.method == "POST":
		if form.is_valid():
			student_number = request.POST.get('ID-number')
			student = get_object_or_404(Student, student_number = student_number)
			students = form.save(commit=False)
			students.student = student
			students.save()
			context['message'] = "Infraction saved"
		else:
			context['message'] = 'Fill in all fields properly'
	else:
		context['form'] = form

		
	return render(request, template_name, context)



def personal_attendance_log(request):
	context = {}
	log_student = StudentAttendance.objects.all()
	log_teacher = TeacherAttendance.objects.all()

	log_student_infractions = StudentInfractions.objects.all()
	log_teacher_infractions = TeacherInfractions.objects.all()

	template_name = 'attendance/personal_attendance_log.html'


	if request.method == "POST":
		
		try:
			student_number = request.POST.get('ID-number')
			
			try:
				student = get_object_or_404(Student, student_number = student_number)
				context['attend'] = student
				
				#cc_log-Cutting Class log
				cc_log = log_student_infractions.filter(Q(student__student_number=student_number),Q(infraction='CC'))
				cc_log = StudentInfractionsTable(cc_log)
				cc_log.paginate(page=request.GET.get('page',1), per_page=5)
				context['cutting_class_log'] = cc_log

				tardy_log = log_student_infractions.filter(Q(student__student_number=student_number), Q(infraction='T'))
				tardy_log = StudentInfractionsTable(tardy_log)
				tardy_log.paginate(page=request.GET.get('page',1), per_page=5)
				context['tardy_log'] = tardy_log

				absent_log = log_student_infractions.filter(Q(student__student_number=student_number),Q(infraction='A'))
				absent_log = StudentInfractionsTable(absent_log)
				cc_log.paginate(page=request.GET.get('page',1), per_page=5)
				context['absent_log'] = absent_log

				log_student = log_student.filter(student__student_number=student_number)
				log_student = StudentAttendanceTable(log_student)
				log_student.paginate(page=request.GET.get('page',1), per_page=25)
				context['personal_attendance_log'] = log_student


			except:
				teacher_number = student_number

				try:
					teacher = get_object_or_404(Teacher, teacher_number = teacher_number)
					context['attend'] = teacher

					log_teacher = log_teacher.filter(teacher__teacher_number=teacher_number)
					log_teacher = StudentAttendanceTable(log_teacher)
					log_teacher.paginate(page=request.GET.get('page',1), per_page=25)
					context['personal_attendance_log'] = log_teacher

				except:
					context['attend'] = 'User Not Found'

		except:
			context['attend'] = 'User Not Found'

	return render(request, template_name, context)



