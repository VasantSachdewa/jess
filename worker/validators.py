from worker.models import JobsDetail

# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class JobsDetailSerializer(ModelSerializer):
    class Meta:
        model = JobsDetail
        fields = [
            "url",
            "id",
            "vendor_id",
            "job_id",
            "page_url",
            "salary_min",
            "salary_max",
            "currency",
            "job_title",
            "company",
            "post_date",
            "job_description",
            "job_requirements",
            "benefits",
            "industry",
        ]
