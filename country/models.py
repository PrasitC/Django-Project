

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    flag = models.ImageField(blank=True)
  
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='countries_created',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='countries_updated', null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name
