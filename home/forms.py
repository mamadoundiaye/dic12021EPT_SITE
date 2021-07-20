from django import forms

#from departements.models import Departement
from django.contrib.auth.models import User
from departements.models import Utilisateur
from departements.models import Etudiant
#EPT SITE ici on gere les formulaire

#formulaire pour l'inscription d'un eleve
class ConnexionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'
