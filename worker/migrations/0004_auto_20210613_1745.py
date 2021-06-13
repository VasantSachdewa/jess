# Generated by Django 3.2.3 on 2021-06-13 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_auto_20210613_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsdetail',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.vendors'),
        ),
        migrations.AlterField(
            model_name='jobsraw',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='worker.jobsdetail'),
        ),
        migrations.AlterField(
            model_name='jobsraw',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.vendors'),
        ),
    ]
