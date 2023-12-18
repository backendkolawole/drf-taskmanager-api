from django.conf import settings
from django.db import models
User = settings.AUTH_USER_MODEL

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name