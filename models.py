from django.db import models

RATED_TYPE = (
        ('0','R'),
        ('1','PG-13'),
        ('2','GENERAL'),
        )

class Movie(models.Model):
    title = models.CharField(max_length=200)
    chinesetitle = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    rated = models.CharField(max_length=1,choices=RATED_TYPE)
    year = models.PositiveIntegerField()
    genres = models.CharField(max_length=200)
    summary = models.TextField()
    fmt = models.CharField(max_length=20)
    length = models.PositiveIntegerField()
    rating = models.FloatField()
    production = models.CharField(max_length=40)
    sn = models.CharField(max_length=20)
    url = models.URLField()
    img = models.URLField()

    def __unicode__(self):
        return self.title
