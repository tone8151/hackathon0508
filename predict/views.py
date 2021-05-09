from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostCreateForm
from matches.models import Match

def predict(request, match_pk):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.match_pk = match_pk
            post.save()
            return redirect('matches:info')
    else:
        form = PostCreateForm()
        match = get_object_or_404(Match, pk=match_pk)
        return render(request, 'predict/predict.html', {'form': form, 'match': match,})

def mypage(request):
    # users_record = Post.objects.filter(author=request.user)
    # num = users_record.count()
    # probs = users_record.values('prob')
    # pred_winners = users_record.values('winner')
    # winners = Match.objects.values('winner')

    # matches_num = Match.objects.values('pk').count()

    # win_or_lose = []

    # for p in range(1, matches_num + 1):
    #     if users_record.get(pk=p).values('winner') == Match.objects.get(pk=p).values('winner'):
    #         win_or_lose.append(1)
    #     else:
    #         win_or_lose.append(0)

    

    # context = {
    #     "wl": win_or_lose,
    #     "winners": winners
    # }
    return render(request, 'predict/mypage.html', {})
