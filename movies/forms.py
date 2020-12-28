from django import forms
from .models import Movie,User
from django.shortcuts import get_object_or_404

#Constants
FORM_FIELD_CLASS='form-control mb-1'

class DateInput(forms.DateInput):
    input_type='date'

class AddMovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['movie_name','movie_release_date','movie_summary']
        widgets={
            'movie_name':forms.TextInput(attrs={'class':FORM_FIELD_CLASS}),
            'movie_release_date':DateInput(attrs={'class':FORM_FIELD_CLASS}),
            'movie_summary':forms.Textarea(attrs={'cols':80,'rows':8,'class':FORM_FIELD_CLASS})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':FORM_FIELD_CLASS}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':FORM_FIELD_CLASS}))
    fields=['username','password']
    def valid_login(self):
        data=self.cleaned_data
        user=data['username']
        pwd=data['password']
        try:
            u=User.objects.get(username=user,password=pwd)
            self.user=u
        except User.DoesNotExist:
            return False
        return True
    def get_user(self):
        return self.user

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','name','password']
        widgets={
            'username':forms.TextInput(attrs={'class':FORM_FIELD_CLASS}),
            'password':forms.PasswordInput(attrs={'class':FORM_FIELD_CLASS})
        }