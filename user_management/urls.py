from django.urls import path
from user_management import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
	path("accounts/signup/", views.CustomSignupView.as_view(), name='user_signup'),
	path("accounts/confirm-email/<key>/", views.CustomConfirmEmailView.as_view(), name='user_confirmation'),
	path("accounts/password/reset/", views.CustomPasswordResetView.as_view(), name='password_reset'),
	path("accounts/login/", views.CustomLoginView.as_view(), name='token_obtain_pair'),
	path("accounts/refresh_token/", TokenRefreshView.as_view(), name='token_refresh'),
]

