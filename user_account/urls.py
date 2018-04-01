from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from user_account.views import newstudentuserView, newteacheruserView

urlpatterns = [
    url(r'^new_student_account/', newstudentuserView, name = 'Student'),
    url(r'^new_teacher_account/', newteacheruserView, name = 'Teacher'),
]