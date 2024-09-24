from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Client Model

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.client_name
    
class Projects(models.Model):
    Project_name = models.CharField(max_length=100)
    client_name = models.ForeignKey(Client,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    





