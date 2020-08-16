from django.shortcuts import render
from reservations.models import Bill, BillType, PaymentMethod, ResState
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsClientOwner
from reservations.serializers import BillSerializer, BillTypeSerializer, PaymentMethodSerializer, ResStateSerializer



# Create your views here.
class BillViewset(viewsets.ModelViewSet):

    serializer_class = BillSerializer

    def get_permissions(self):

        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []

        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsClientOwner]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsClientOwner]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsClientOwner]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsClientOwner]
        elif self.action == 'destroy':
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Bill.objects.filter(user=self.kwargs['client_pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        #set's client id according to the one sent on url
        self.request.data["user"] = self.kwargs["client_pk"]
        return super(BillViewset, self).create(request, *args, **kwargs)



class BillTypeViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = BillTypeSerializer
    queryset = BillType.objects.all()


class PaymentMethodViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()

class ResStateViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ResStateSerializer
    queryset = ResState.objects.all()
