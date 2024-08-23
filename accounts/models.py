from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model to extend Django's built-in User model
class CustomUser(AbstractUser):
    """Custom user model to add additional fields."""
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# Model for storing questions
class Question(models.Model):
    """Model to store questions."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(help_text="Enter the question text.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
