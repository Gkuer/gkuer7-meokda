from django.shortcuts import render, redirect
from .models import board
from .forms import BoardForm
from django.http import Http404
from user.models import meokda_user
from django.core.paginator import Paginator
from tag.models import Tag
# Create your views here.

def board_detail(request, pk):
    try:
        boards = board.objects.get(pk=pk)
    except board.DoesNotExist:
        raise Http404('해당 게시글이 없습니다')
    return render(request, 'board_detail.html', {'board': boards})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            meokdauser = meokda_user.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            boards = board()
            boards.title = form.cleaned_data['title']
            boards.contents = form.cleaned_data['contents']
            boards.writer = meokdauser
            boards.save()

            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                boards.tags.add(_tag)

            return redirect('/board/list/')
    form = BoardForm()
    return render(request, 'board_write.html', {'form' : form})


def board_list(request):
    all_boards = board.objects.all().order_by('-id')
    page = int(request.GET.get('p',1))
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards':boards})