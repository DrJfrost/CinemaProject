from reservations.models import BillType, PaymentMethod, ResState, Reservation, Bill
from movies.models import Spot, Show
from movies.serializers import SpotInfoSerializer
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

class ReservationInfoSerializer(serializers.ModelSerializer):

    state = ResStateSerializer()
    spots = SpotInfoSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ['id', 'description', 'scoring', 'state', 'spots', 'show']

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'description', 'scoring', 'state', 'spots', 'show']
    
    def validate(self, data):

        if ('show' in data and not 'spots' in data) or (not 'show' in data and 'spots' in data):
            raise serializers.ValidationError('you need to provide spots and show if you want to update them')

        show = data["show"]
        for spot in data["spots"]:
            print((str)(spot.room)+' '+(str)(show.room))
            if spot.room != show.room:
                raise serializers.ValidationError({'spots': 'the spot "'+(str)(spot.id)+'"does not belong to the room of the show that is being reservated make sure that you choose a spot of the same room where the show is taking place'})
        return data

class BillInfoSerializer(serializers.ModelSerializer):

    payment_method = PaymentMethodSerializer()
    bill_type = BillTypeSerializer()
    reservation = ReservationInfoSerializer()

    class Meta:
        model = Bill
        fields = ['id', 'value', 'user', 'bill_type', 'payment_method', 'reservation']
        read_only_fields = ['value']

class BillSerializer(serializers.ModelSerializer):

    reservation = ReservationSerializer()

    class Meta:
        model = Bill
        fields = ['id', 'value', 'user', 'bill_type', 'payment_method', 'reservation']
        read_only_fields = ['value']

    def create(self, validated_data):

        #reservation info
        reservation_data = validated_data.pop('reservation')
        spots = reservation_data.pop('spots')

        #calculation of total reservation value according to selected spots
        value = 0
        for spot in spots:
            value += spot.value

        #creation of reservation
        reservation = Reservation.objects.create(**reservation_data)
        reservation.spots.add(*spots)
        reservation.save()

        bill = Bill.objects.create(value=value, reservation=reservation, **validated_data)


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
