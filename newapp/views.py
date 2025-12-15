from django.shortcuts import render
from .models import Movies

# Create your views here.
def movie_list(request):
    movie_objects = Movies.objects.all()
    return render(request, 'newapp/movie_list.html', {'movie_objects': movie_objects})