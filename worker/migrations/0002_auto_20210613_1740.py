# Generated by Django 3.2.3 on 2021-06-13 06:51

from django.db import migrations

def add_jobsdb_vendor(apps, schedma_editor):
    Vendors = apps.get_model('worker', 'Vendors')
    jobsdb_vendor = Vendors.objects.create(
        name='jobsdb',
        url='https://www.jobsdb.com'
    )
    jobsdb_vendor.save()


def rollback_jobsdb_vendor(apps, schedma_editor):
    Vendors = apps.get_model('worker', 'Vendors')
    jobsdb_vendor = Vendors.objects.get(name='jobsdb')
    jobsdb_vendor.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_jobsdb_vendor, rollback_jobsdb_vendor),
    ]