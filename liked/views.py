from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from movies.models import Movie

@login_required
def index(request):
    # Only movies liked by this user
    liked_movies = Movie.objects.filter(likes=request.user)

    template_data = {
        'title': 'My Liked Movies',
        'movies': liked_movies
    }

    return render(request, 'liked/index.html', {'template_data': template_data})
