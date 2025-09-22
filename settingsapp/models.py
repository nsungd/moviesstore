from django.db import models
from django.contrib.auth.models import User

class SecuritySetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_question = models.CharField(max_length=255)
    security_answer = models.CharField(max_length=255)

    def __str__(self):
        return f"Security settings for {self.user.username}"

class SecurityQuestion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.question}"
