from django.shortcuts import render
from users.models import User, Position
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from users.permissions import IsSuperUser, IsStaffOwner, IsStaff, IsOwner
from users.serializers import EmployeeSerializer, ClientSerializer, PositionSerializer



# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):

    serializer_class = EmployeeSerializer
    queryset = User.objects.filter(is_staff=True)

    def get_permissions(self):

        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsSuperUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsStaffOwner]
        elif self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsStaffOwner]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]

        return [permission() for permission in permission_classes]

class ClientViewset(viewsets.ModelViewSet):

    def get_permissions(self):

        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsStaff]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]

        return [permission() for permission in permission_classes]

    serializer_class = ClientSerializer
    queryset = User.objects.filter(is_staff=False)

class PositionViewset(viewsets.ModelViewSet):

    serializer_class = PositionSerializer
    queryset = Position.objects.all()