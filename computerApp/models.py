from django.db import models
from datetime import datetime, date

class Machine(models.Model):
    TYPE = (
        ('PC', 'PC - Run windows'),
        ('Mac', 'Mac - Run MacOs'),
        ('Serveur', 'Serveur - Simple Serveur to deploy virtual machines'),
        ('Switch', 'Switch - To maintains and connect servers'),
    )
    ETAT_CHOICES = (
        ('En ligne', 'En ligne'),
        ('Hors ligne', 'Hors ligne'),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

    maintenanceDate = models.DateField(default=datetime.now())
    type = models.CharField(max_length=32, choices=TYPE, default='PC')
    ip = models.CharField(max_length=15, default='0.0.0.0')
    etat = models.CharField(max_length=32, choices=ETAT_CHOICES, default='En ligne')
    date_maintenance = models.DateField(default=date.today)
    mise_a_jour = models.DateTimeField(auto_now=True)

class Personnel(models.Model):
    TYPE = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Non spécifié', 'Non spécifié'),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE, default='Non spécifié')

    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom



