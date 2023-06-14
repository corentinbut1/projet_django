# Generated by Django 4.1.7 on 2023-06-05 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0019_personnel_type_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personnel",
            name="type",
        ),
        migrations.AddField(
            model_name="personnel",
            name="typep",
            field=models.CharField(
                choices=[
                    ("Homme", "Homme"),
                    ("Femme", "Femme"),
                    ("Non spécifié", "Non spécifié"),
                ],
                default="Non spécifié",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 5, 15, 49, 43, 256711)
            ),
        ),
    ]