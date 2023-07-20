from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=10)
    description = models.TextField()
    technology = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

