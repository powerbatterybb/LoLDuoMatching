"""이전버전
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "post/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "post/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "post/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "post/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("post:results", args=(question.id,)))
"""

# 최신튜토_4
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from post.forms import PostForm
from django.shortcuts import redirect

from .models import Post, Comment
from django.utils import timezone

# 게시글 렌더링 추가
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'post/index.html', context)

# 게시글 상세 페이지 추가


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # comments = post.comments.filter(approved_comment=True)
    return render(request, 'post/post_detail.html', {'post': post})
    # return render(request, 'post/post_detail.html', {'post': post, 'comments': comments})

def post_register(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:index')
    else:
        form = PostForm()
    return render(request, 'post/post_register.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:index')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post:index')

# def comment_delete(request, pk, comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.method == 'POST':
#         comment.delete()
#     return redirect('post_detail', pk=pk)