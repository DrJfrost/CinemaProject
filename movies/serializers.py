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

    class Meta:
        model = SpotType
        fields = ['id', 'name']

class RoomSerializer(serializers.ModelSerializer):

    headquarter = serializers.PrimaryKeyRelatedField(required=True, queryset=Headquarter.objects.all())
    
    class Meta:
        model = Room
        fields = ['id', 'name', 'headquarter', 'spots']
        read_only_fiels = ['spots']
        depth = 1

class MovieInfoSerializer(serializers.ModelSerializer):

    genre = MovieGenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'duration', 'genre']

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'name', 'duration', 'genre']

class ShowSerializer(serializers.ModelSerializer):

    room = serializers.PrimaryKeyRelatedField(required=True, queryset=Room.objects.all())
    movie = serializers.PrimaryKeyRelatedField(required=True, queryset=Movie.objects.all())

    class Meta:
        model = Show
        fields = ['id', 'name', 'start', 'end', 'scoring', 'room', 'movie']
        depth = 1

class SpotInfoSerializer(serializers.ModelSerializer):

    spot_type = SpotTypeSerializer()

    class Meta:
        model = Spot
        fields = ['id', 'name', 'row', 'col', 'value', 'spot_type', 'room'] 

class SpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spot
        fields = ['id', 'name', 'row', 'col', 'value', 'spot_type', 'room'] 