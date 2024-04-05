from django import forms 
from .models import MovieReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReviewModel
        fields = ['Rating']