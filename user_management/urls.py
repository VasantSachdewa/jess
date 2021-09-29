from django.conf.urls import include, url
from django.urls import path, re_path
from rest_framework import urlpatterns
from user_management import views


urlpatterns = [
	path("accounts/signup/", views.CustomSignupView.as_view(), name='user_signup'),
	path("accounts/confirm-email/<key>/", views.CustomConfirmEmailView.as_view(), name='user_confirmation')
]

