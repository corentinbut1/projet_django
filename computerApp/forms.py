import re
from django import forms
from django.core.exceptions import ValidationError
from computerApp.models import Machine
from computerApp.models import Personnel
from django.forms import DateInput


class AddMachineForm(forms.Form) :


    Type = [
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOs' )),
        ('Serveur', ('Serveur - Simple Serveur to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    ]
    ETAT_CHOICES = [
        ('En ligne', 'En ligne'),
        ('Hors ligne', 'Hors ligne'),  
    ]
    nom = forms.CharField(required=True, label='Nom de la machine')
    type = forms.ChoiceField(choices=Type, label='Type de la machine')
    ip = forms.GenericIPAddressField(label="Adresse ip")
    etat = forms.ChoiceField(choices=ETAT_CHOICES, label='État de la machine')
    date_maintenance = forms.DateField(widget=DateInput(attrs={'type': 'date'}), label='Date de maintenance')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 200:
            raise ValidationError(("Erreur de format poutr le champ nom"))
        return data  

    def clean_ip(self):
        data = self.cleaned_data["ip"]
        address = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if not (re.search(address, data)):
            raise ValidationError(("erreur de format pour le champs addresse ip"))
        return data

      
class DeleteMachineForm(forms.Form):
    machine_id = forms.ModelChoiceField(queryset=Machine.objects.all())

    def delete_machine(self):
        machine = self.cleaned_data.get('machine_id')
        if machine:
            machine.delete()


class AddPersonnelForm(forms.Form) :
    
    TYPE = [
        ('Homme', ('Homme')),
        ('Femme', ('Femme')),
        ('Non spécifié', ('Non spécifié')),
    ]
    nom = forms.CharField(required=True, label='Nom Personne')
    type = forms.ChoiceField(choices=TYPE, label='Genre')



    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 200:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data


class DeletePersonnelForm(forms.Form):
    personnel_id = forms.ModelChoiceField(queryset=Personnel.objects.all())

    def delete_personnel(self):
        personnel = self.cleaned_data.get('personnel_id')
        if personnel:
            personnel.delete()

class UpdateMachineForm(forms.Form):
    ETAT_CHOICES = [
        ('En ligne', 'En ligne'),
        ('Hors ligne', 'Hors ligne'),  
    ]
    etat = forms.ChoiceField(choices=ETAT_CHOICES, label='État de la machine')