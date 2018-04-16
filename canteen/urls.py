from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from canteen.views import ConsumableView, ReloadBalance, ViewBalance, PurchaseView
from canteen.views import account_balance, canteen_in, canteen, order

urlpatterns = [
	#url(r'^balance/$', ViewBalance, name = "balance"),
	url(r'^consumable/$', ConsumableView, name = "consumable"),
	url(r'^purchase/$', PurchaseView, name = "purchase"),
	url(r'^reload/$', ReloadBalance, name = "reload"),

	url(r'^balance/$', account_balance, name = "balance"),
	url(r'^enter_main/$', canteen_in, name="order"),
	url(r'^ip_unit/$', canteen),
	url(r'^enter_new_main/$', order),
]