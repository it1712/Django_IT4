from django.forms import ModelForm
from .models import *


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genres', 'description', 'release_year', 'directors', 'writers', 'runtime', 'score', 'cast', 'img']
