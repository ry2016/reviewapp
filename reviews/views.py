from django.shortcuts import render
from django.http import HttpResponseRedirect
# Register your models here.
from .models import Restaurant, Review 
from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from reviews.forms import ReviewForm
from django.db.models import Q # new

# Main index page for the reviews app
def Account(request):
    return render(request, 'reviews/account.html')

def index(request):
    return render(request, 'reviews/index2.html')

def About(request):
    return render(request,'reviews/about.html')

def Cafes(request):
    return render(request,'reviews/cafes.html')  

def Campus(request):
    return render(request,'reviews/campus.html')     
    
# The list of restaurants (restaurant_list.html)
class RestaurantListView(generic.ListView):
    model = Restaurant

def RestaurantList(request):
    """View function for home page of site."""

    # Generate lists of different types of restaurants
    restaurants = Restaurant.objects.all()
    restaurantsRestaurant = Restaurant.objects.filter(style='Restaurant')
    restaurantsCafe = Restaurant.objects.filter(style='Café')
    restaurantsMarket = Restaurant.objects.filter(style='Market')
    

    context = {
        'restaurants': restaurants,
        'restaurantsRestaurant': restaurantsRestaurant,
        'restaurantsCafe': restaurantsCafe,
        'restaurantsMarket': restaurantsMarket,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'reviews/restaurant_list.html', context=context)

def RestaurantSearch(request):
    """View function for home page of site."""

    if request.method == "GET":
        query_name = request.GET.get('q', None)
        if query_name:
            if query_name.lower() == "cafe":
                query_name = "Café"
            results = Restaurant.objects.filter(
            Q(name__icontains=query_name) | Q(style__icontains=query_name)
            )
            return render(request, 'reviews/restaurant_search.html', {"results":results, "query":query_name})
        else:
            results = Restaurant.objects.all()
            return render(request, 'reviews/restaurant_search.html', {"results":results})


# The details of a single restaurant (restaurant_details.html)
def RestaurantDetails(request, restaurant_id):
    restaurantObj = get_object_or_404(Restaurant, pk=restaurant_id)
    reviews = Review.objects.filter(resturaunt=restaurantObj)

    # If the form was submitted
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ReviewForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            review = form.save(commit=False)
            review.username = form.cleaned_data['username']
            review.text = form.cleaned_data['text']
            review.rating = form.cleaned_data['rating']
            review.resturaunt = restaurantObj
            review.save()

            # redirect to a new URL:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form = ReviewForm()

       
    context = {
        'form': form,
        'restaurant': restaurantObj,
        'reviews': reviews, 
    }

    return render(request, 'reviews/restaurant_details.html', context=context)