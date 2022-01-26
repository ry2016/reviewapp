# Models a.k.a. databases
from django.db import models
from django.utils import timezone
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.

# Type of food a restaurant serves (used for sorting by restaurant type)
class FoodType(models.Model):
    """Model representing a type of food."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# Describes a restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    foodtype = models.ManyToManyField(FoodType, help_text='Select the type of resturaunt')

    def __str__(self):
        """String for representing the restaurant"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail for this restaurant."""
        return reverse('restaurant-detail', args=[str(self.id)])


RATINGS = [
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars'),
]

# Describes a review left by a user
class Review(models.Model):
    resturaunt = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField( auto_now_add=True)
    text = models.CharField(max_length=3000)
    rating = models.PositiveSmallIntegerField(choices=RATINGS)