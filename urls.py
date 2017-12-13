from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views import generic
from pymovieshelf import views

urlpatterns = [
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^movies/$',views.MoviesList.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$',views.MovieDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
