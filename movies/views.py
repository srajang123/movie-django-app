from django.shortcuts import render,reverse,get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Movie
from .forms import AddMovieForm
# Create your views here.
class HomeView(generic.ListView):
    template_name='movies/Home.html'
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
    if request.method=='POST':
        form=AddMovieForm(request.POST)
        if form.is_valid():
            post=form.save()
            return HttpResponseRedirect(reverse('movies:Home'))
    else:
        form=AddMovieForm()
    return render(request,'movies/Add.html',{'form':form})

def updatemovieview(request,pk):
    movie=get_object_or_404(Movie,pk=pk)
    if request.method=='POST':
        form=AddMovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('movies:Home'))
    else:
        form=AddMovieForm(instance=movie)
    return render(request,'movies/EditMovie.html',{'form':form,'id':pk})
