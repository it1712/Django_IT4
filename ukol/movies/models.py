from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a movie genre (e. g. Science Fiction)')

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=100, help_text='Enter studio name (e. g. Warner Bros. Pictures)')

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    death = models.DateField(null=True, blank=True, help_text='Leave empty if alive')

    def __str__(self):
        out = f"{self.first_name} {self.surname}, *{self.birth}"
        if self.death is not None:
            out += f" †{self.death}"
        return out


class Writer(models.Model):
    writer = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    movies = models.ManyToManyField('Movie')


class Director(models.Model):
    director = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    movies = models.ManyToManyField('Movie')


class Actor(models.Model):
    actor = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    movies = models.ManyToManyField('Movie')


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField('Genre')
    description = models.TextField(null=True)
    release_year = models.PositiveIntegerField()
    directors = models.ManyToManyField('Director')
    writers = models.ManyToManyField('Writer')
    studio = models.ForeignKey('Studio', on_delete=models.DO_NOTHING)
    runtime = models.IntegerField()
    score = models.IntegerField()
    cast = models.ManyToManyField('Actor')

    def __str__(self):
        return f"{self.title} ({self.release_year}), {self.directors}, {self.studio}, {self.genres}, {self.runtime}, {self.score}, {self.cast}, {self.description}"

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])
