# Generated by Django 4.1.7 on 2023-05-11 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0006_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 11, 8, 58, 33, 21399)
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="nom",
            field=models.CharField(max_length=6),
        ),
    ]
