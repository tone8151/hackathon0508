from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from . import forms
from matches.models import Match

def index(request, pk):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.match_pk = pk
            post.save()
            return redirect('info/')
    else:
       form = forms.PostForm()
       match = get_object_or_404(Match, pk=pk)
    return render(request, 'predict/index.html', {'form': form, 'match': match})

