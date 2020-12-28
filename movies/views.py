from django.shortcuts import render,reverse,get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import AddMovieForm,LoginForm,RegisterForm

#Constants
HOME_PAGE='movies:Home'


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

@login_required(login_url='/login')
def addmovieview(request):
    print(request.user)
    if request.method=='POST':
        form=AddMovieForm(request.POST)
        if form.is_valid():
            post=form.save()
            return HttpResponseRedirect(reverse(HOME_PAGE))
    else:
        form=AddMovieForm()
    return render(request,'movies/Add.html',{'form':form})

def updatemovieview(request,pk):
    movie=get_object_or_404(Movie,pk=pk)
    if request.method=='POST':
        form=AddMovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(HOME_PAGE))
    else:
        form=AddMovieForm(instance=movie)
    return render(request,'movies/EditMovie.html',{'form':form,'id':pk,'movie':movie.movie_name})

def loginview(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            if form.valid_login():
                user=form.get_user()
                login(request,user)
                return HttpResponseRedirect(reverse(HOME_PAGE))
    else:
        form=LoginForm()
    return render(request,'movies/Login.html',{'form':form})

def registerview(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            print(user)
            print(type(user))
            login(request,user)
            return HttpResponseRedirect(reverse(HOME_PAGE))
    else:
        form=RegisterForm()
    return render(request,'movies/Register.html',{'form':form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('movies:Login'))