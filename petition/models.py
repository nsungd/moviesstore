from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)  # short title for the petition
    description = models.TextField()          # why this movie should be added
    movie_name = models.CharField(max_length=255)  # requested movie name
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petitions")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Petition {self.id}: {self.movie_name} by {self.created_by.username}"

    @property
    def total_votes(self):
        return self.votes.count()


class PetitionVote(models.Model):
    id = models.AutoField(primary_key=True)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('petition', 'user')  # prevent duplicate votes

    def __str__(self):
        return f"{self.user.username} voted on {self.petition.movie_name}"
