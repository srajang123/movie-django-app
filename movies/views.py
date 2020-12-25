from django.shortcuts import render,reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Movie
# Create your views here.
class HomeView(generic.ListView):
    template_name='movies/Home.html'
    def get_queryset(self):
        return 

class AddView(generic.ListView):
    template_name='movies/Add.html'
    def get_queryset(self):
        return

class MoviesView(generic.ListView):
    template_name='movies/View.html'
    context_object_name='movies_list'
    def get_queryset(self):
        return Movie.objects.all()
    
class EditView(generic.ListView):
    template_name='movies/Edit.html'
    def get_queryset(self):
        return
    
    

def AddMovieView(request):
    movie_name=request.POST['movie_name']
    movie_release_date=request.POST['movie_release_date']
    movie_summary=request.POST['movie_summary']
    return HttpResponseRedirect(reverse('movies:Home'))

