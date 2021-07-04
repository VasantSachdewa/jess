from django.urls import path, include
from rest_framework import routers
from worker import views

router = routers.DefaultRouter()
router.register(r'jobs', views.JobDetailViewSet)



urlpatterns = [
	path('', include(router.urls))
]