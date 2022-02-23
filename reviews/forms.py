# Defining forms that users can input data into in html files
from django import forms
from reviews.models import Review, RATINGS
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ReviewForm, form that allows users to leave a review for a specific restaurant
class ReviewForm(forms.ModelForm):
    username = forms.CharField(max_length=3000, required=True)
    text = forms.CharField(max_length=3000, required=True)
    rating = forms.ChoiceField(choices=RATINGS, required=False)

    class Meta:
        model = Review
        fields = ('username','text', 'rating')

# SignUpForm, allows users to create an account
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
