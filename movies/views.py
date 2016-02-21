from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', { 'movies': movies })

def show(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/show.html', { 'movie': movie })