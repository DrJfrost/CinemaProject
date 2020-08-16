from movies.models import Headquarter, MovieGenre, SpotType, Room, Movie, Show, Spot
from rest_framework import serializers

class HeadquarterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headquarter
        fields = ['id', 'name']

class MovieGenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieGenre
        fields = ['id', 'name']

class SpotTypeSerializer(serializers.ModelSerializer):

    class meta:
        model = SpotType
        fields = ['id', 'name']

class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        field = ['id', 'name', 'headquarter']
        depth = 1

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'name', 'duration', 'genre']
        depth = 1

class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        fields = ['id', 'name', 'start', 'end', 'scoring', 'room', 'movie']
        depth = 1

class SpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spot
        fields = ['id', 'name', 'row', 'col', 'value', 'spot_type', 'room'] 
        depth = 1