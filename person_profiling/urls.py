from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from person_profiling.views import attendance, infractions, personal_attendance_log

urlpatterns = [
    url(r'^attendance/$', attendance, name = "attendance"),
    url(r'^infractions/$', infractions, name = "infractions"),
    url(r'^log/$', personal_attendance_log, name = "log"),
]