from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from movies.models import *


def index(req):
    return render(req, template_name='index.html')


class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movie_list.html'
    extra_context = {
        'nadpis': 'Movie list'
    }


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'
    extra_context = {
        'nadpis': 'Movie detail'
    }


class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'genres', 'description', 'release_year', 'directors', 'writers', 'runtime', 'score', 'cast', 'img']
    extra_context = {
        'nadpis': 'Create movie',
    }


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'genres', 'description', 'release_year', 'directors', 'writers', 'runtime', 'score', 'cast', 'img']
    extra_context = {
        'nadpis': 'Edit movie',
    }


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('list')
