from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from canteen.views import ConsumableView, ReloadBalance, ViewBalance, PurchaseView

urlpatterns = [
	url(r'^balance/$', ViewBalance, name = "balance"),
	url(r'^consumable/$', ConsumableView, name = "consumable"),
	url(r'^purchase/$', PurchaseView, name = "purchase"),
	url(r'^reload/$', ReloadBalance, name = "reload"),
]