from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSereializer
from .models import Hero

# Create your views here.
# ModelViewSet will handle GET and POST for Heroes

class HeroViewSet(viewsets.ModelViewSet):
  queryset = Hero.objects.all().order_by("name")
  serializer_class = HeroSereializer