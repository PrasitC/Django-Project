

# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    flag = models.URLField()
  
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return self.name
