from django import forms
from .models import Movie
class DateInput(forms.DateInput):
    input_type='date'

class AddMovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['movie_name','movie_release_date','movie_summary']
        widgets={
            'movie_name':forms.TextInput(attrs={'class':'form-control  mb-1'}),
            'movie_release_date':DateInput(attrs={'class':'form-control mb-1'}),
            'movie_summary':forms.Textarea(attrs={'cols':80,'rows':8,'class':'form-control mb-1'})
        }