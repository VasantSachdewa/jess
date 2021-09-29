from django.conf.urls import include, url
from django.urls import path
from rest_framework import urlpatterns
from user_management import views


urlpatterns = [
	path("signup", views.CustomSignupView.as_view(), name='user_signup')
]

