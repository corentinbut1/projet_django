# Generated by Django 4.1.7 on 2023-06-07 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0028_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 7, 23, 13, 45, 981300)
            ),
        ),
    ]
