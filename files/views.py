from rest_framework import generics
from files.serializers import FileSerializer
from .models import Files

# Create your views here.
class FileView(generics.ListCreateAPIView):
    queryset= Files.objects.all()
    serializer_class= FileSerializer
