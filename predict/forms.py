from django import forms
from .models import Post
from matches.models import Match

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = (
            'prob',
            'winner',
        )