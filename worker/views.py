from django.core.paginator import Page
from worker.models import JobsDetail
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from worker.validators import JobsDetailSerializer
from jess.libs.metrics_tracker import counter


class StandardPaginationConfig(PageNumberPagination):
    page_size_query_param = 'pageSize'
    max_page_size = 10


# Create your views here.
class JobDetailViewSet(ReadOnlyModelViewSet):
    queryset = JobsDetail.objects.all()
    serializer_class = JobsDetailSerializer
    pagination_class = StandardPaginationConfig

    @counter('worker.JobDetailViewSet.list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
