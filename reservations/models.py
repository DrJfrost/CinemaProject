from django.db import models
from users.models import User
from movies.models import Spot, Show

class BillType(models.Model):
    name = models.CharField(max_length=25)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=25)

class ResState(models.Model):

    name = models.CharField(max_length=30)

class Reservation(models.Model):
    
    creation = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    scoring = models.PositiveIntegerField(default=0)

    #foreign keys
    state = models.ForeignKey(ResState, on_delete=models.PROTECT, default=1, verbose_name='state of the reservation')
    spots = models.ManyToManyField(Spot, verbose_name='spots that were booked')
    show = models.ForeignKey(Show, on_delete=models.PROTECT, verbose_name='movie that was booked')


class Bill(models.Model):
    
    value = models.FloatField()
    
    #foreign keys
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='client owner of the bill')
    bill_type = models.ForeignKey(BillType, on_delete=models.PROTECT, verbose_name='billing type')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, verbose_name='payment method of the bill')
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, verbose_name='reservation of the bill', related_name='reservation')
# Create your models here.
