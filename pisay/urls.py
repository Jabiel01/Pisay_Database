"""pisay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from laboratory import urls as laboratory_urls
from library import urls as library_urls
from person_profiling import urls as person_profiling_urls
from canteen import urls as canteen_urls
from user_account import urls as user_account_urls

from pisay.views import homeview, aboutview, admissionview


urlpatterns = [
    url(r'^about/$', aboutview, name = "about"),
    url(r'^admin/', admin.site.urls),
    url(r'^admission/', admissionview, name="admission"),
    url(r'^attendance/', include(person_profiling_urls, namespace='person')),
    url(r'^canteen/', include(canteen_urls, namespace = 'canteen')),
    url(r'^home/$', homeview, name = "home"),
    url(r'^laboratory/', include(laboratory_urls, namespace='laboratory')),
    url(r'^library/', include(library_urls, namespace='library')),
    url(r'^new_user/', include(user_account_urls, namespace = 'new_user')),
]
