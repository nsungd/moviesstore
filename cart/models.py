from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class Order(models.Model):
    REGION_CHOICES = [
        ('NA', 'North America'),
        ('EU', 'Europe'),
        ('AS', 'Asia'),
        ('SA', 'South America'),
        ('AF', 'Africa'),
        ('OC', 'Oceania'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    region = models.CharField(max_length=2, choices=REGION_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username} ({self.get_region_display()})"


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.name} x{self.quantity}"
