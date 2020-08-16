from django.shortcuts import render
from movies.models import Headquarter, Room, Spot, SpotType, MovieGenre, Show
from rest_framework import viewsets
from movies.serializers import HeadquarterSerializer, RoomSerializer, SpotSerializer, SpotTypeSerializer, MovieGenreSerializer, ShowSerializer



# Create your views here.

class SpotViewset(viewsets.ModelViewSet):

    serializer_class = SpotSerializer

    def get_queryset(self):
        queryset = Spot.objects.filter(room=self.kwargs['room_pk'])
        return queryset

class RoomViewset(viewsets.ModelViewSet):

    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.filter(headquarter=self.kwargs['headquarter_pk'])
        return queryset


class HeadquarterViewset(viewsets.ModelViewSet):

    serializer_class = HeadquarterSerializer
    queryset = Headquarter.objects.all()


class SpotTypeViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = SpotTypeSerializer
    queryset = SpotType.objects.all()

class MovieGenreViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = MovieGenreSerializer
    queryset = MovieGenre.objects.all()

class ShowViewset(viewsets.ModelViewSet):

    serializer_class = ShowSerializer

    def get_queryset(self):
        queryset = Show.objects.filter(room__headquarter=self.kwargs['headquarter_pk'])
        return queryset