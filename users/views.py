from django.shortcuts import render
from users.models import User, Position
from rest_framework import viewsets
from users.serializers import EmployeeSerializer, ClientSerializer, PositionSerializer



# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):

    serializer_class = EmployeeSerializer
    queryset = User.objects.filter(is_staff=True)

class ClientViewset(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = User.objects.filter(is_staff=False)

class PositionViewset(viewsets.ModelViewSet):

    serializer_class = PositionSerializer
    queryset = Position.objects.all()