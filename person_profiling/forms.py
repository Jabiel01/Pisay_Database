from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateTimeField

from person_profiling.models import Student, StudentInfractions, Teacher, TeacherInfractions

sections = (
			('1', '7-Diamond'),
			('2', '7-Gold'),
			('3', '7-Pearl'),
			('4', '8-Dahlia'),
			('5', '8-Kamia'),
			('6', '8-Rosal'),
			('7', '9-Calcium'),
			('8', '9-Lithium'),
			('9', '9-Sodium'),
			('10', '10-Electron'),
			('11', '10-Neutron'),
			('12', '10-Proton'),
			('13', '11-Curie'),
			('14', '11-Darwin'),
			('15', '11-Einstein'),
			('16', '11-Franklin'),
			('17', '11-Newton'),
			('18', '12-Farad'),
			('19', '12-Hertz'),
			('20', '12-Kelvin'),
			('21', '12-Pascal'),
			('22', '12-Tesla'),
	)

class StudentForm(UserCreationForm):
	first_name = forms.CharField(max_length = 100)
	middle_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	student_number = forms.IntegerField()
	section = forms.ChoiceField(choices = sections, required = True)
	

	class Meta:
	    model = User
	    fields = ( 'first_name', 'middle_name','last_name', 'student_number', 'username', 'password1', 'password2', )

class TeacherForm(UserCreationForm):
	first_name = forms.CharField(max_length = 100)
	middle_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	teacher_number = forms.IntegerField()

	class Meta:
	    model = User
	    fields = ( 'first_name', 'middle_name','last_name', 'teacher_number', 'username', 'password1', 'password2', )


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
