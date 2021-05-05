from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from datetime import date


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=100, help_text='Enter a movie genre (e. g. Science Fiction)')

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    death = models.DateField(null=True, blank=True, help_text='Leave empty if alive')

    def __str__(self):
        # out = f"{self.first_name} {self.surname} *{self.birth}"
        # if self.death is not None:
        #     out += f" †{self.death}"
        # return out
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name_plural = 'People'


class Writer(models.Model):
    writer = models.OneToOneField('Person', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.writer}"


class Director(models.Model):
    director = models.OneToOneField('Person', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.director}"


class Actor(models.Model):
    actor = models.OneToOneField('Person', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.actor}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField('Genre')
    description = models.TextField(null=True)
    release_year = models.PositiveIntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(10 + int(date.today().year))])
    directors = models.ManyToManyField('Director')
    writers = models.ManyToManyField('Writer')
    runtime = models.IntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)])
    score = models.IntegerField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    cast = models.ManyToManyField('Actor')
    img = models.ImageField(upload_to='movies/%Y/%m/%d', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        out =  f"{self.title} ({self.release_year}), "
        out += ", ".join(str(d) for d in self.directors.all()) + ", "
        out += ", ".join(str(g) for g in self.genres.all()) + ", "
        out += f"{self.runtime}, {self.score}, "
        out += ", ".join(str(c) for c in self.cast.all()) + ", "
        out += f"{self.description[0:30]}..."
        return out

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        ordering = ["score", "title"]
