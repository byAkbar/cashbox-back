from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=True)    
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groups', null=True)
 
 
    def __str__(self):
        return self.username