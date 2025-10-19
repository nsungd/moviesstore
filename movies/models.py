from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    # Remove old ManyToMany likes — we’ll use Like model instead

    def __str__(self):
        return f"{self.id} - {self.name}"

    def total_likes(self):
        return self.like_set.filter(value=1).count()

    def total_dislikes(self):
        return self.like_set.filter(value=-1).count()

    def average_rating(self):
        likes = self.total_likes()
        dislikes = self.total_dislikes()
        total = likes + dislikes
        if total == 0:
            return 0  # Avoid division by zero
        percentage = (likes / total) * 100
        return round(percentage, 1)  # e.g. 76.5%

    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name
    
class Like(models.Model):
    VALUE_CHOICES = [
        (1, 'Like'),
        (-1, 'Dislike'),
        (0, 'Neutral'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VALUE_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} rated {self.movie.name}: {self.get_value_display()}"