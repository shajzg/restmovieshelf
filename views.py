
#=======================REST API=========================
from rest_framework import generics
from pymovieshelf.models import Movie
from pymovieshelf.serializers import MovieSerializer

class MoviesList(generics.ListCreateAPIView):
    """
    List all movies , or create a new movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a movie instance.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
