from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    ref_country = models.CharField(max_length=255)
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True)
    flag = models.ImageField(blank=True)
  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='city_created', null=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, related_name='city_updated', null=True, on_delete=models.SET_NULL)
  
    def __str__(self):
        return self.name