from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime

class Match(models.Model):

    CHOICE_CAT = [
        ('boxing', 'BOXING'),
        ('wrestling', 'WRESTLING'),
        ('sumo', 'SUMO'),
    ]

    CHOICE_WIN = [
        ('TBD', 'TBD'),
        ('player1', 'player1'),
        ('player2', 'player2'),
    ]

    category = models.CharField(max_length=30, choices=CHOICE_CAT, default='boxing')
    title = models.CharField(max_length=50)
    player1 = models.CharField(max_length=30)
    player2 = models.CharField(max_length=30)
    match_date = models.DateTimeField(default=timezone.now)
    outline = models.TextField(max_length=500)
    winner = models.CharField(max_length=30, choices=CHOICE_WIN, default='TBD')
   
    def __str__(self):
        return self.title
