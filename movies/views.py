from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', { 'movies': movies })

def show(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/show.html', { 'movie': movie })

def new(request):
    return render(request, 'movies/new.html')
