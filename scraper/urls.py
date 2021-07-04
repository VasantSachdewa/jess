from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "config/", views.WebsiteConfig.as_view(), name="website_configuration"
    ),
    path("sync_jobs/", views.SyncJob.as_view(), name="sync_jobs"),
]
