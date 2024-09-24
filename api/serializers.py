from rest_framework import serializers
from api.models import Client,Projects


class ClientSerializer(serializers.HyperlinkedModelSerializer):
   client_id  = serializers.ReadOnlyField() 
   class Meta:
      model=Client 
      fields ="__all__"

class ProjectSerializer(serializers.ModelSerializer):
   id  = serializers.ReadOnlyField()    
   class Meta:
      model=Projects
      fields = "__all__"

