from typing import Dict
from django.db import models

# Create your models here.


class Vendors(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, blank=False, null=False, unique=True
    )
    url = models.URLField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    def to_dict(self) -> Dict:
        return {"id": self.vendor_id, "name": self.name, "url": self.url}


class JobsDetail(models.Model):
    class Meta:
        unique_together = (("vendor_id", "job_id"),)

    id = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    job_id = models.CharField(max_length=255)
    page_url = models.URLField(max_length=200, blank=False, null=False)
    salary_min = models.FloatField(default=None, null=True)
    salary_max = models.FloatField(default=None, null=True)
    currency = models.CharField(max_length=4, default=None, null=True)
    job_title = models.CharField(max_length=255, blank=False, null=False)
    company = models.CharField(max_length=255, blank=False)
    post_date = models.DateTimeField(blank=False, null=False)
    job_description = models.JSONField(blank=False)
    job_requirements = models.JSONField(blank=False)
    benefits = models.JSONField(blank=False)
    industry = models.CharField(max_length=255, blank=False)


class JobsRaw(models.Model):
    class Meta:
        unique_together = (("vendor_id", "job_id"),)

    id = models.ForeignKey(
        JobsDetail, on_delete=models.CASCADE, primary_key=True
    )
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    job_id = models.CharField(max_length=255)
    raw_data = models.JSONField(blank=False)

    def __str__(self) -> str:
        return self.job_id
