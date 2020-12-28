from django.urls import path
from . import views
app_name='movies'
urlpatterns = [
    path('',views.HomeView.as_view(),name='Home'),
    path('login',views.loginview,name='Login'),
    path('register',views.registerview,name='Register'),
    path('add',views.addmovieview,name='Add'),
    path('addmovie',views.addmovieview,name='AddMovie'),
    path('view',views.MoviesView.as_view(),name='View'),
    path('edit',views.EditView.as_view(),name='Edit'),
    path('edit/<int:pk>',views.updatemovieview,name='EditMovie'),
    path('update/<int:pk>',views.updatemovieview,name='UpdateMovie')
]
