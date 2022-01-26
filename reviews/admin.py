# Controls what databases are able to be viewed on the admin site ("localhost:8000/admin/")
from django.contrib import admin

# Register models.
from .models import FoodType, Restaurant, Review 
admin.site.register(FoodType)
admin.site.register(Restaurant)
admin.site.register(Review)