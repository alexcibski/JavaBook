from django.db import models
from django.urls import reverse

RATE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)
ROAST = (
    ('L', 'Light'),
    ('M', 'Medium'),
    ('D', 'Dark')
)

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    roast = models.CharField(
        'Roast',
        max_length=1,
        choices = ROAST
    )
    countryOfOrigin = models.CharField(max_length=100, blank=True)
    tastingNotes = models.CharField(max_length=100, blank=True)
    rating = models.CharField(
        'Rating',
        max_length=1,
        choices = RATE
    )
    review = models.TextField(max_length=250, blank=True)
    brewTips = models.TextField(max_length=250, blank=True)
    image = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('coffee_detail', kwargs={'coffee_id': self.id})
    
class Maker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    rating = models.CharField(
        'Rating',
        max_length=1,
        choices = RATE
    )
    description = models.TextField(blank=True)
    review = models.TextField(blank=True)
    brewTips = models.TextField(blank=True)
    image = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('maker_detail', kwargs={'maker_id': self.id})