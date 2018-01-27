from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views import generic
from pymovieshelf import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/auth/login/$',obtain_jwt_token,name='api-login'),
    url(r'^movies/$',views.MoviesList.as_view(),name="movie-list"),
    url(r'^movies/create/$',views.MovieCreate.as_view(),name="movie-create"),
    url(r'^movies/(?P<pk>[0-9]+)/$',views.MovieDetail.as_view()),
    url(r'^movies/latest/$',views.LatestAddedMovies.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
