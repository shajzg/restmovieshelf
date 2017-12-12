from django.conf.urls import *
from pymovieshelf.views import ListCreateMovies
from django.views import generic
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_imdb/', views.add_imdb),
    url(r'^searchmovie/', views.searchmovie),
    url(r'^(?P<pk>\d+)/$',views.MovieDetailView.as_view()),
    url(r'^api/movies',ListCreateMovies.as_view(),name='list_movies'),
]
