from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from laboratory.views import MaterialView 

urlpatterns = [
	url(r'^material/$', MaterialView, name = "material"),
]