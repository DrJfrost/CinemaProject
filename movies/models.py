from django.db import models

# Create your models here.
class Headquarter(models.Model):
    
    name = models.CharField('name of the headquarter', max_length=100)


class MovieGenre(models.Model):

    Name = models.CharField('name of the movie genre', max_length=30)


class SpotType(models.Model):

    name = models.CharField('name of the spot type', max_length=100)
    value = models.FloatField()

class Room(models.Model):

    name = models.CharField('name of the room', max_length=100)

    #foreign keys
    headquarter = models.ForeignKey(Headquarter, on_delete=models.PROTECT, verbose_name='headqwuarter where the room belongs', related_name='rooms')

class Movie(models.Model):

    name = models.CharField('name of the movie', max_length=100)
    duration = models.DurationField('duration of the movie')

    #foreign keys
    genre = models.ManyToManyField(MovieGenre, verbose_name='genre of the movie')

class Show(models.Model):

    name = models.CharField('name of the show', max_length=100)
    start = models.DateTimeField('start date of show')
    end = models.DateTimeField('end date of show')
    scoring = models.PositiveIntegerField('scoring of the show')

    #foreign keys
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name='room of the show')
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, verbose_name='movie of the show')


class Spot(models.Model):

    name = models.CharField(max_length=100)
    row = models.PositiveIntegerField()
    col = models.PositiveIntegerField()
    value = models.FloatField()

    #foreign keys
    spot_type = models.ForeignKey(SpotType, on_delete=models.PROTECT, verbose_name='spot type')
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name='room of the spot')
