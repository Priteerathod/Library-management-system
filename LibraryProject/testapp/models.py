from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.FloatField()
    p_date=models.DateField()
    def get_absolute_url(self):
        return reverse('list')
