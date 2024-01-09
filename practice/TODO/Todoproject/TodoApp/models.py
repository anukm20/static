from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=25)
    priority=models.IntegerField()
    
    
    def __str__(self):
        return self.task