from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatters = [
	url(r'^student_profiling/', include('student_profiling.urls')),
	url(r'^admin/', admin.site.urls),
]