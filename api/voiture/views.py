from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VoitureSerializer
from .models import Voiture




class VoitureView(viewsets.ModelViewSet):
    serializer_class = VoitureSerializer
    queryset = Voiture.objects.all()

   