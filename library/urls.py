from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from library.views import Borrow_Book, Search_Book, Personal_Library_Card

urlpatterns = [
    url(r'^borrow/$', Borrow_Book, name = "borrow"),
    url(r'^search/$', Search_Book, name = 'search'),
    url(r'^view_card/$', Personal_Library_Card, name = "log"),
]