from django.shortcuts import render
from cnab.serializers import CnabSerializer
from .models import Cnab
from rest_framework import generics
# Create your views here.
class CnabView(generics.ListCreateAPIView):
    queryset = Cnab.objects.all()
    serializer_class= CnabSerializer