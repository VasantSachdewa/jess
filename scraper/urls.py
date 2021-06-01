from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('config/', views.WebsiteConfig.as_view(), name='website_configuration'),
]