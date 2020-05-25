from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ProductView, OrderView, NewOrderView, ClientView, AuthSmsView


app_name = "water"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('products/', ProductView.as_view()),
    path('orders/', OrderView.as_view()),
    path('neworder/', NewOrderView.as_view()),
    path('client/', ClientView.as_view()),
    path('auth/', AuthSmsView.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
