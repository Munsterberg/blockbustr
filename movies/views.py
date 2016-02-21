from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    data = ', '.join([str(movie) for movie in movies])
    return HttpResponse(data)