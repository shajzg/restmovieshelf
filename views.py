
#=======================REST API=========================
from rest_framework import generics,permissions
from pymovieshelf.models import Movie
from pymovieshelf.serializers import MovieSerializer

class MoviesList(generics.ListAPIView):
    """
    List all movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreate(generics.CreateAPIView):
    """
    create a new movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a movie instance.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAdminUser,)

class LatestAddedMovies(generics.ListAPIView):
    """
    List latest added 4 movies
    """
    queryset = Movie.objects.all().order_by('-id')[:4]
    serializer_class = MovieSerializer
