from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    template_name = "movie_list.html"
    model = Movie
    context_object_name = 'sw_movies'


class MovieDetail(DetailView):
    template_name = 'movie_detail.html'
    model = Movie
