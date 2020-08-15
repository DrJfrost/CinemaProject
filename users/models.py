from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Identification(models.Model):
    id = models.CharField('identification of a user', max_length=25, primary_key=True)


class User(AbstractUser):
    first_name = models.CharField("user's first name", max_length=30)
    last_name = models.CharField("user's last name", max_length=150)
    email = models.EmailField("user's email addresss")
    phone = PhoneNumberField()
    
    #foreign keys
    identification = models.OneToOneField(Identification, on_delete=models.PROTECT, verbose_name='identification of a user')

class Position(models.Model):

    name = models.CharField(max_length=30)


class Contract(models.Model):

    salary = models.FloatField()
    join_date = models.DateTimeField('joid date of the employee')
    end_date = models.DateField('ending date of employee contract')
    is_active = models.BooleanField('state of the contract', default=True)
    
    #foreign keys
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user owner of the contract', related_name='contract')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='position of the employee')


class ClientProfile(models.Model):
    score = models.FloatField()
    address = models.TextField()

    #foreign keys
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user owner of the customer profile', related_name='client_profile')


