

from rest_framework import serializers
from .models import Voiture

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = ('id', 'marque', 'matricule', 'kilometrages', 'assurance', 'vignette','personnelle','travail')

    
        