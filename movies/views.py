from multiprocessing import context
from re import M
from urllib import request
from django.shortcuts import render, redirect

from movies.models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def new(request):
    context = {
        'genres': ['Comedy', 'Horror', 'Action', 'SF', 'Thriller', 'Romance'],
    }
    return render(request,'movies/new.html', context)


def create(request):
    movie = Movie(
        title = request.POST.get('title'), 
        audience = request.POST.get('audience'),
        release_date = request.POST.get('release_date'),
        genre = request.POST.get('genre'),
        score = request.POST.get('score'),
        poster_url = request.POST.get('poster_url'),
        description = request.POST.get('description'))
    movie.save()
    return redirect('movies:index')


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request,'movies/detail.html',context)


def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
        'genres': ['Comedy', 'Horror', 'Action', 'SF', 'Thriller', 'Romance'],
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title') 
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    return redirect('movies:detail', movie.pk)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')