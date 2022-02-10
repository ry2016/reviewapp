# Defining forms that users can input data into in html files
from django import forms
from reviews.models import Review, RATINGS

# ReviewForm, form that allows users to leave a review for a specific restaurant
class ReviewForm(forms.ModelForm):
    username = forms.CharField(max_length=3000, required=True)
    text = forms.CharField(max_length=3000, required=True)
    rating = forms.ChoiceField(choices=RATINGS, required=False)

    class Meta:
        model = Review
        fields = ('username','text', 'rating')
