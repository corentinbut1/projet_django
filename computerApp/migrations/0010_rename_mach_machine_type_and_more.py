# Generated by Django 4.1.7 on 2023-05-22 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0009_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="machine",
            old_name="mach",
            new_name="type",
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 5, 22, 8, 22, 29, 936832)
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="nom",
            field=models.CharField(max_length=200),
        ),
    ]
