
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from api.models import Client , Projects
from api.serializers import ClientSerializer,ProjectSerializer
from api.forms import UserRegister
from rest_framework.decorators import action

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

