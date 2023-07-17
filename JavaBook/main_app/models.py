from django.db import models
from django.urls import reverse

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    countryOfOrigin = models.CharField(max_length=100)
    tastingNotes = models.CharField(max_length=100)
    rating = models.IntegerField()
    review = models.TextField(max_length=250)
    brewTips = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('coffee_detail', kwargs={'coffee_id': self.id})
    
class Maker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.TextField()
    review = models.TextField()
    brewTips = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('maker_detail', kwargs={'maker_id': self.id})