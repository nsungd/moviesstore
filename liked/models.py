from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie   # import your Movie model

class LikedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_movies_list")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="liked_by_users")
    date_liked = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')  # prevent duplicate likes

    def __str__(self):
        return f"{self.user.username} liked {self.movie.name}"
