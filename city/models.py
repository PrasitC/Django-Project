

# Create your models here.
from django.db import models

class City(models.Model):
    ref_country=models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    flag = models.URLField()
  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
