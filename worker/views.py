from django.core.paginator import Page
from worker.models import JobsDetail
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from worker.validators import JobsDetailSerializer
from jess.libs.metrics_tracker import counter, timer


class StandardPaginationConfig(PageNumberPagination):
    page_size_query_param = 'pageSize'
    max_page_size = 10


# Create your views here.
class JobDetailViewSet(ReadOnlyModelViewSet):
    queryset = JobsDetail.objects.all()
    serializer_class = JobsDetailSerializer
    pagination_class = StandardPaginationConfig

    @timer('worker.JobDetailViewSet.list')
    @counter('worker.JobDetailViewSet.list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @timer('worker.JobDetailViewSet.filter_queryset')
    @counter('worker.JobDetailViewSet.filter_queryset')
    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)

    @timer('worker.JobDetailViewSet.get_queryset')
    @counter('worker.JobDetailViewSet.get_queryset')
    def get_queryset(self):
        return super().get_queryset()

    @timer('worker.JobDetailViewSet.paginate_queryset')
    @counter('worker.JobDetailViewSet.paginate_queryset')
    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)

    @timer('worker.JobDetailViewSet.get_paginated_response')
    @counter('worker.JobDetailViewSet.get_paginated_response')
    def get_paginated_response(self, data):
        return super().get_paginated_response(data)

    @timer('worker.JobDetailViewSet.get-serializer')
    @counter('worker.JobDetailViewSet.get-serializer')
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)
