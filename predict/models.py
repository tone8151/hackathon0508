from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    prob = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_date = models.DateTimeField(default=timezone.now)
    match_pk = models.IntegerField(null=True)

    CHOICES = [
        ('player1', 'player1'),
        ('player2', 'player2'),
    ]
    
    winner = models.CharField(max_length=50, choices=CHOICES, default='ali')

    def __str__(self):
        return self.author.username