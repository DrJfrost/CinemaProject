from reservations.models import BillType, PaymentMethod, ResState, Reservation, Bill
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

    class Meta:
        model = Reservation
        fields = ['id', 'description', 'scoring', 'state', 'spots', 'show']
        depth = 1


class BillSerializer(serializers.ModelSerializer):

    reservation = ReservationSerializer()

    class Meta:
        model = Bill
        fields = ['id', 'value', 'user', 'bill_type', 'payment_method', 'reservation']
        depth = 1

    def create(self, validated_data):

        #reservation info
        reservation_data = validated_data.pop('reservation')
        spots = reservation_data.pop('spots')

        bill = Bill.objects.create(**validated_data)

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