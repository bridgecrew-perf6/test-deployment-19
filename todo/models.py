from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    

    def __str__(self):
        return self.name


