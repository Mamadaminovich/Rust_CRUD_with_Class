from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    time = models.TimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title