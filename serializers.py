from pymovieshelf.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):

    fmt = serializers.SerializerMethodField()
    rated = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        #fields = ('title','chinesetitle','year')
        fields = '__all__'

    def get_fmt(self,obj):
        return obj.get_fmt_display()

    def get_rated(self,obj):
        return obj.get_rated_display()

