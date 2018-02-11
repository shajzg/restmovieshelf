"""
diffrence between v1 and v2

3,15d2
< RATED_TYPE = (
<         ('0','R'),
<         ('1','PG-13'),
<         ('2','GENERAL'),
<         )
<
< FORMAT_TYPE = (
<         ('0','Blu-Ray'),
<         ('1','Blu-Ray 3D'),
<         ('2','DVD'),
<         ('3','Blu-Ray 4K')
<         )
<
19,20d5
<     director = models.CharField(max_length=100)
<     rated = models.CharField(max_length=1,choices=RATED_TYPE,default='0')
22a8
>     director = models.CharField(max_length=100)
24c10
<     fmt = models.CharField(max_length=1,choices=FORMAT_TYPE)
---
>     fmt = models.CharField(max_length=20)
27,28d12
<     production = models.CharField(max_length=40,default='')
<     sn = models.CharField(max_length=20,default='')

"""
from django.db import models

RATED_TYPE = (
        ('0','R'),
        ('1','PG-13'),
        ('2','GENERAL'),
        )

FORMAT_TYPE = (
        ('0','Blu-Ray'),
        ('1','Blu-Ray 3D'),
        ('2','DVD'),
        ('3','Blu-Ray 4K'),
)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    chinesetitle = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    rated = models.CharField(max_length=1,choices=RATED_TYPE)
    year = models.PositiveIntegerField()
    genres = models.CharField(max_length=200)
    summary = models.TextField()
    fmt = models.CharField(max_length=1,choices=FORMAT_TYPE)
    length = models.CharField(max_length=50)
    rating = models.FloatField()
    production = models.CharField(max_length=40,default='')
    sn = models.CharField(max_length=20,default='')
    url = models.URLField(default='http://blue-ray.win/pymovieshelf/')
    img = models.URLField(default='')

    def __unicode__(self):
        return self.title
