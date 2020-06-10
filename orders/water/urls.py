from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view

from .views import AuthSmsView
from .views import ClientView
from .views import ConfirmAuthView
from .views import NewOrderView
from .views import OrderView
from .views import ReportView

# schema_view = get_swagger_view(title='Pastebin API')

# urlpatterns = [
#    url(r'^$', schema_view)
# ]

schema_view = get_swagger_view(title="Swagger Docs")

app_name = "water"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    # path('products/', ProductView.as_view()),
    path("orders/", OrderView.as_view()),
    path("neworder/", NewOrderView.as_view()),
    path("client/", ClientView.as_view()),
    path("auth/", AuthSmsView.as_view()),
    path("confirm/", ConfirmAuthView.as_view()),
    path("report/", ReportView.as_view())
    # path('swagger/', schema_view),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
