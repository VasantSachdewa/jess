from worker.models import JobsDetail
from rest_framework import viewsets
from worker.validators import JobsDetailSerializer


# Create your views here.
class JobDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobsDetail.objects.all()
    serializer_class = JobsDetailSerializer
