from django.shortcuts import get_object_or_404, render
from post.forms import PostForm, CommentForm
from django.shortcuts import redirect

from .models import Post, Comment


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'post/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post:post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'post/post_detail.html', {'post': post, 'form': form, 'comments': comments})


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


def comment_delete(request, pk, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
    return redirect('post:post_detail', pk=pk)
