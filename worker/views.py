from django.core.paginator import Page
from worker.models import JobsDetail
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from worker.validators import JobsDetailSerializer


class StandardPaginationConfig(PageNumberPagination):
    page_size_query_param = 'pageSize'
    max_page_size = 10


# Create your views here.
class JobDetailViewSet(ReadOnlyModelViewSet):
    queryset = JobsDetail.objects.all()
    serializer_class = JobsDetailSerializer
    pagination_class = StandardPaginationConfig
