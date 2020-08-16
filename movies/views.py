from django.shortcuts import render
from movies.models import Headquarter, Room, Spot, SpotType, MovieGenre, Show, Movie
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, SAFE_METHODS
from users.permissions import IsStaff, IsSuperUser
from movies.permissions import CheckRoom
from movies.serializers import (HeadquarterSerializer, RoomSerializer, SpotSerializer, SpotInfoSerializer, SpotTypeSerializer, 
                                    MovieGenreSerializer, ShowSerializer, MovieSerializer, MovieInfoSerializer)



# Create your views here.

class SpotViewset(viewsets.ModelViewSet):

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

    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return SpotSerializer
        return SpotInfoSerializer
    
    def create(self, request, *args, **kwargs):
        #set's room id according to the one sent on url
        self.request.data["room"] = self.kwargs["room_pk"]
        return super(SpotViewset, self).create(request, *args, **kwargs)

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

    def create(self, request, *args, **kwargs):
        #set's headquarter id according to the one sent on url
        self.request.data["headquarter"] = self.kwargs["headquarter_pk"]
        return super(RoomViewset, self).create(request, *args, **kwargs)


class HeadquarterViewset(viewsets.ModelViewSet):

    serializer_class = HeadquarterSerializer
    queryset = Headquarter.objects.all()

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
            permission_classes = [IsStaff, CheckRoom]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsStaff, CheckRoom]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Show.objects.filter(room__headquarter=self.kwargs['headquarter_pk'])
        return queryset

class MovieViewset(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    
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

    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return MovieSerializer
        return MovieInfoSerializer