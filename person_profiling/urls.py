from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from person_profiling.views import attendance, infractions

urlpatterns = [
    url(r'^attendance/$', attendance, name="attendance"),
    url(r'^infractions/$', infractions.as_view(), name = 'infractions'),
]