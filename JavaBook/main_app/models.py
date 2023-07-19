from django.db import models
from django.urls import reverse

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    roast = models.CharField(max_length=100, blank=True)
    countryOfOrigin = models.CharField(max_length=100, blank=True)
    tastingNotes = models.CharField(max_length=100, blank=True)
    rating = models.PositiveIntegerField()
    review = models.TextField(max_length=250, blank=True)
    brewTips = models.TextField(max_length=250, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('coffee_detail', kwargs={'coffee_id': self.id})
    
class Maker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    review = models.TextField(blank=True)
    brewTips = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('maker_detail', kwargs={'maker_id': self.id})