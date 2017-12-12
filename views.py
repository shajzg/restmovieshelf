from django.shortcuts import render_to_response, redirect,render
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import imdb
from pymovieshelf.models import Movie
from django.contrib.auth.decorators import user_passes_test
import re
import simplejson as json
from django.core import serializers

from django.views.generic import ListView,DetailView

class MovieList(ListView):
    model = Movie

class MovieDetailView(DetailView):
    queryset = Movie.objects.all()
    def get_object(self):
	object = super(MovieDetailView,self).get_object()
        object.save()
        return object

def staff_required(login_url=None):
        return user_passes_test(lambda u: u.is_staff, login_url=login_url)

def index(request):
    return render(request,'pymovieshelf/index.html')

@staff_required(login_url='/admin/')
def add_imdb(request):
    if request.POST and 'select' in request.POST:
        i = imdb.IMDb()
        try:
            m = i.get_movie(request.POST['movie_id'])
        except imdb.IMDbError:
            return render_to_response('pymovieshelf/add_imdb.html',
                    {'error': 'Failed to fetch movie info.',},
                    context_instance=RequestContext(request))

        try:
            t = m['canonical title'].strip()
        except KeyError:
            t = ''

        try:
            g = ', '.join(m['genres'])
        except KeyError:
            g = ''

        try:
            y = m['year']
        except KeyError:
            y = ''

        try:
            d = m['director'][0]['name']
        except KeyError:
            d = ''

        try:
            rt = m['rating']
        except KeyError:
            rt = ''

        try:
            c = m['full-size cover url'].strip()
        except KeyError:
            c = ''

        try:
            s = m['plot summary'][0][:m['plot summary'][0].rfind('::')]
        except KeyError:
            s = ''

        try:
            r = re.sub(r'(USA\:)?(?P<runtime>\d+).*', r'\g<runtime>', m['runtime'][0])
            # for films not release in USA
	    if r.find(":") > 0:
	    	r = r.split(":")[1]
        except KeyError:
            r = 0

        newmovie = Movie(title=t, fmt=request.POST['format'], genres=g, year=y,
                         summary=s, length=r, img=c,director=d,rating=rt,
                         url='http://www.imdb.com/title/tt%s/' %
                         (request.POST['movie_id'], ))
        newmovie.save()
        return redirect('/admin/pymovieshelf/movie/')
    elif request.POST and 'title' in request.POST:
        i = imdb.IMDb()
        movie_list = i.search_movie(request.POST['title'])
        return render_to_response('pymovieshelf/add_imdb.html',
                {'movie_list': movie_list, },
                context_instance=RequestContext(request))
    else:
        return render_to_response('pymovieshelf/add_imdb.html',
                {},
                context_instance=RequestContext(request))
@csrf_exempt
def search(request):
    if request.POST and 'title' in request.POST:
	searchtype = request.POST['search']
        if searchtype == "entitle":
        	movie_list = Movie.objects.filter(title__icontains=request.POST['title']).order_by('-rating')
        if searchtype == "cntitle":
        	movie_list = Movie.objects.filter(chinesetitle__icontains=request.POST['title']).order_by('-rating')
        if searchtype == "director":
        	movie_list = Movie.objects.filter(director__icontains=request.POST['title']).order_by('-rating')
        return render_to_response('pymovieshelf/movie_list.html',
                {'object_list': movie_list,},
                context_instance=RequestContext(request))
    else:
        return redirect('/pymovieshelf/')

@csrf_exempt
def searchmovie(request):
    # post with json data
    rtnjson = "[]"
    if request.method == 'POST':
        try:
            json_postdata = json.loads(request.body)
            searchtype = json_postdata['searchtype']
            moviecontent = json_postdata['moviecontent']
            if moviecontent:
                if searchtype == "entitle":
                        movie_list = Movie.objects.filter(title__icontains=moviecontent)
                if searchtype == "cntitle":
                        movie_list = Movie.objects.filter(chinesetitle__icontains=moviecontent)
                if searchtype == "director":
                        movie_list = Movie.objects.filter(director__icontains=moviecontent)
            else:
                movie_list = Movie.objects.all()
            rtnjson = serializers.serialize('json',movie_list)
            return HttpResponse(rtnjson,"application/json")
        except:
            return HttpResponse(rtnjson,"application/json")
    else:
        return HttpResponse(rtnjson,"application/json")

#=======================REST API=========================
from rest_framework import generics
from pymovieshelf.serializers import MovieSerializer

class ListCreateMovies(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
