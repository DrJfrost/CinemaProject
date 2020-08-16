from django.shortcuts import render
from movies.models import Headquarter, Room, Spot, SpotType, MovieGenre, Show
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.permissions import IsStaff, IsSuperUser
from movies.serializers import HeadquarterSerializer, RoomSerializer, SpotSerializer, SpotTypeSerializer, MovieGenreSerializer, ShowSerializer



# Create your views here.

class SpotViewset(viewsets.ModelViewSet):

    serializer_class = SpotSerializer

    def get_queryset(self):
        queryset = Spot.objects.filter(room=self.kwargs['room_pk'])
        return queryset
    
    def get_permissions(self):

        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []

        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsStaff]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]

        return [permission() for permission in permission_classes]

class RoomViewset(viewsets.ModelViewSet):

    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.filter(headquarter=self.kwargs['headquarter_pk'])
        return queryset
    
    def get_permissions(self):

        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []

        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsStaff]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]

        return [permission() for permission in permission_classes]


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

    def get_permissions(self):

        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []

        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsStaff]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Show.objects.filter(room__headquarter=self.kwargs['headquarter_pk'])
        return queryset