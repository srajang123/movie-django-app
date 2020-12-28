from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=300)
    movie_release_date=models.DateField()
    movie_summary=models.CharField(max_length=10000)
    def __str__(self):
        return self.movie_name+', released on '+str(self.movie_release_date)

class User(AbstractUser,models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=400)
    name=models.CharField(max_length=100)
    class Meta(AbstractUser.Meta):
        swappable='AUTH_USER_MODEL'
    def __str__(self):
        return self.name+' has username '+self.username