from reservations.models import BillType, PaymentMethod, ResState, Reservation, Bill
from movies.models import Spot, Show
from users.models import User
from rest_framework import serializers

class BillTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillType
        fields = ['id', 'name']


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ['id', 'name']


class ResStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResState
        fields = ['id', 'name']


class ReservationSerializer(serializers.ModelSerializer):

    state = serializers.PrimaryKeyRelatedField(read_only=True)
    spots = serializers.PrimaryKeyRelatedField(required=True, queryset=Spot.objects.all(), many=True)
    show = serializers.PrimaryKeyRelatedField(required=True, queryset=Show.objects.all())

    class Meta:
        model = Reservation
        fields = ['id', 'description', 'scoring', 'state', 'spots', 'show']
        depth = 1


class BillSerializer(serializers.ModelSerializer):

    reservation = ReservationSerializer()
    user = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.filter(is_staff=False))
    bill_type = serializers.PrimaryKeyRelatedField(required=True, queryset=BillType.objects.all())
    payment_method = serializers.PrimaryKeyRelatedField(required=True, queryset=PaymentMethod.objects.all())

    class Meta:
        model = Bill
        fields = ['id', 'value', 'user', 'bill_type', 'payment_method', 'reservation']
        read_only_fields = ['value']
        depth = 1

    def create(self, validated_data):

        #reservation info
        reservation_data = validated_data.pop('reservation')
        spots = reservation_data.pop('spots')

        #calculation of total reservation value according to selected spots
        value = 0
        for spot in spots:
            value += spot.value

        bill = Bill.objects.create(value=value, **validated_data)

        reservation = Reservation.objects.create(**reservation_data)
        reservation.spots.add(**spots)
        reservation.save()


        bill.save()
        
        return bill

    def update(self, instance, validated_data):

        #reservation info
        reservation_data = validated_data.pop('reservation')
        reservation = instance.reservation

        instance.value = validated_data.get('value', instance.value)
        instance.saved_score = validated_data.get('saved_score', instance.saved_score)
        instance.bill_type = validated_data.get('bill_tytpe', instance.bill_type)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)

        if 'reservation' in validated_data:
            reservation.description = reservation_data.get('description', reservation.description)
            reservation.scoring = reservation_data.get('scoring', reservation.scoring)
            reservation.state = reservation_data.get('state', reservation.state)
            if 'spots' in reservation_data:
                reservation.spots.clear()
                reservation.spots.add(**reservation_data.get('spots'))
            reservation.save()
        
        instance.save()

        return instance