from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', { 'movies': movies })

def show(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/show.html', { 'movie': movie })

def new(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('/movies/')
    else:
        form = MovieForm()
    return render(request, 'movies/new.html', { 'form': form })
