from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=300)
    movie_release_date=models.DateField()
    movie_summary=models.CharField(max_length=10000)
    def __str__(self):
        return self.movie_name+', released on '+str(self.movie_release_date)