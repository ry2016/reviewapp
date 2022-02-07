# Models a.k.a. databases
from django.db import models
from django.utils import timezone
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.


# Describes a restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="description")
    location = models.CharField(max_length=200, default="location")
    style = models.CharField(max_length=30)

    # String for representing the restaurant
    def __str__(self):

        return self.name
    
    # Returns the url to access a detail for this restaurant
    def get_absolute_url(self):
        return reverse('restaurant-detail', args=[str(self.id)])

    # Returns average rating that the restaurant has
    def get_reviews(self):
        reviews = Review.objects.filter(resturaunt=self.id)
        if len(reviews) > 0: # if the restaurant has at least 1 review
            total = 0
            for review in reviews:
                total += review.rating
            return round(total/len(reviews),2)
        else:
            return 0



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