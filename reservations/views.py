from django.shortcuts import render
from reservations.models import Bill, BillType, PaymentMethod, ResState
from rest_framework import viewsets
from reservations.serializers import BillSerializer, BillTypeSerializer, PaymentMethodSerializer, ResStateSerializer



# Create your views here.
class BillViewset(viewsets.ModelViewSet):

    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = Bill.objects.filter(user=self.kwargs['client_pk'])
        return queryset


class BillTypeViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = BillTypeSerializer
    queryset = BillType.objects.all()


class PaymentMethodViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()

class ResStateViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ResStateSerializer
    queryset = ResState.objects.all()
