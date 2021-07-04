# Generated by Django 3.2.3 on 2021-06-13 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendors",
            fields=[
                (
                    "vendor_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("url", models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="JobsDetail",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("job_id", models.CharField(max_length=255)),
                ("page_url", models.URLField()),
                ("salary_min", models.FloatField(default=None, null=True)),
                ("salary_max", models.FloatField(default=None, null=True)),
                (
                    "currency",
                    models.CharField(default=None, max_length=4, null=True),
                ),
                ("job_title", models.CharField(max_length=255)),
                ("company", models.CharField(max_length=255)),
                ("post_date", models.DateTimeField()),
                ("job_description", models.TextField()),
                ("job_requirements", models.TextField()),
                ("benefits", models.TextField()),
                ("industry", models.CharField(max_length=255)),
                (
                    "vendor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="worker.vendors",
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobsRaw",
            fields=[
                (
                    "id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="worker.jobsdetail",
                    ),
                ),
                ("job_id", models.CharField(max_length=255)),
                ("raw_data", models.JSONField()),
                (
                    "vendor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="worker.vendors",
                    ),
                ),
            ],
        ),
    ]
