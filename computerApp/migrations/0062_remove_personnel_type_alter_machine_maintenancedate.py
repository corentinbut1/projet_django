# Generated by Django 4.1.7 on 2023-06-09 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0061_machine_mise_a_jour_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personnel",
            name="type",
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 9, 1, 2, 47, 106909)
            ),
        ),
    ]
