from django.urls import path

from .views import AuthSmsView
from .views import ClientView
from .views import NewOrderView
from .views import OrderView
from .views import ProductView

app_name = "water"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path("products/", ProductView.as_view()),
    path("orders/", OrderView.as_view()),
    path("neworder/", NewOrderView.as_view()),
    path("client/", ClientView.as_view()),
    path("auth/sms/", AuthSmsView.as_view()),
]