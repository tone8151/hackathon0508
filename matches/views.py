from django.shortcuts import render, get_object_or_404
from .models import Match

def info(request):
    matches = Match.objects.filter(match_date__year=2021)
    return render(request, 'matches/info.html', {'matches': matches})