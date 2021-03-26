from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Language, Paradigm, Programmer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
# Create your views here.

# viewsets.ModelViewSet - Handle all the HTTP Methods.
class LanguageViewSet(viewsets.ModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # Allow read-only premissions


class ParadigmViewSet(viewsets.ModelViewSet):
	queryset = Paradigm.objects.all()
	serializer_class = ParadigmSerializer

	#! 'permission_classes' default is "IsAuthenticated"


class ProgrammerViewSet(viewsets.ModelViewSet):
	queryset = Programmer.objects.all()
	serializer_class = ProgrammerSerializer

	#! 'permission_classes' default is "IsAuthenticated"

	

