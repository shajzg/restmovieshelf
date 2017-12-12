from pymovieshelf.models import Movie
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','chinesetitle','year')
    search_fields = ['title','chinesetitle']

admin.site.register(Movie,MovieAdmin)

