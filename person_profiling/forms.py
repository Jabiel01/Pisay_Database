from django import forms

from person_profiling.models import Student, Teacher

class StudentForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = ('__all__')
		# fields = ('first_name', 'last_name')

class TeacherForm(forms.ModelForm):
	
	class Meta:
		model = Teacher
		fields = ('__all__')
