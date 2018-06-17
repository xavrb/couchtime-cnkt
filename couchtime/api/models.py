from django.db import models

# Create your models here.

class movie(models.Model):
    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    cast = models.CharField(max_length=500)
    director = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    country = models.CharField(max_length=20)
    comment = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)




def __str__(self):
    return '%s %s %s %s %s %s %s' % (
        self.title,
        self.genre,
        self.cast,
        self.director,
        self.year,
        self.country,
        self.comment,
        self.rating,
        self.created_at
    )
