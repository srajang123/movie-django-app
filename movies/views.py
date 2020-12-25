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
    context_object_name='movies_list'
    def get_queryset(self):
        return Movie.objects.all()

class EditMovieView(generic.DetailView):
    model=Movie
    template_name='movies/EditMovie.html'

def addmovieview(request):
    movie_name=request.POST['movie_name']
    movie_release_date=request.POST['movie_release_date']
    movie_summary=request.POST['movie_summary']
    m=Movie(movie_name=movie_name,movie_release_date=movie_release_date,movie_summary=movie_summary)
    m.save()
    return HttpResponseRedirect(reverse('movies:Home'))

def updatemovieview(request):
    movie_id=request.POST['movie_id']
    movie_name=request.POST['movie_name']
    movie_release_date=request.POST['movie_release_date']
    movie_summary=request.POST['movie_summary']
    m=Movie.objects.get(pk=movie_id)
    m.movie_name=movie_name
    m.movie_release_date=movie_release_date
    m.movie_summary=movie_summary
    m.save()
    return HttpResponseRedirect(reverse('movies:Home'))