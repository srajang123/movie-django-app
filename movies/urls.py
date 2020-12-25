from django.urls import path
from . import views
app_name='movies'
urlpatterns = [
    path('',views.HomeView.as_view(),name='Home'),
    path('add',views.AddView.as_view(),name='Add'),
    path('addmovie',views.AddMovieView,name='AddMovie'),
    path('view',views.MoviesView.as_view(),name='View'),
    path('edit',views.EditView.as_view(),name='Edit')
]