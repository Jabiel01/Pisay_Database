from django import forms
from django.contrib.admin import widgets
from django.forms import DateTimeField

from person_profiling.models import Student, StudentInfractions, Teacher, TeacherInfractions

class StudentForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = ('__all__')
		# fields = ('first_name', 'last_name')

class TeacherForm(forms.ModelForm):
	
	class Meta:
		model = Teacher
		fields = ('__all__')

class StudentInfractionsForm(forms.ModelForm):
	
	class Meta:
		model = StudentInfractions
		fields = ('infraction','reason','date_incurred')

	def __init__(self, *args, **kwargs):
		super(StudentInfractionsForm, self).__init__(*args, **kwargs)
		#self.fields['date_incurred'].widget = widgets.AdminSplitDateTime()
		self.fields['date_incurred'] = DateTimeField(input_formats=["%d %b %Y %H:%M:%S"])

class TeacerInfractionsForm(forms.ModelForm):

	class Meta:
		model = TeacherInfractions
		fields = ('__all__')
