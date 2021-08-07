from rest_framework import serializers
from departements.models import Etudiant

class EtudiantSerializer(serializers.ModelSerializer):
	class Meta:
		#authentification : inscription et login 
		model = Etudiant
		fields = '__all__'
