from django.shortcuts import get_object_or_404, render
from post.forms import PostForm, CommentForm
from django.shortcuts import redirect
from .forms import SignUpForm
from .models import Post, Comment

def index(request):
    posts = Post.objects.all()
    query = request.GET.get('q')
    # context = {'posts': posts}

    if query:
        search_results = Post.objects.filter(title__icontains=query)
    else:
        search_results = None
    return render(request, 'post/index.html', {'posts': posts, 'search_results': search_results})
    # return render(request, 'post/index.html', context)



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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:index')  # 회원가입 후 로그인 페이지로 리다이렉트
    else:
        form = SignUpForm()
    return render(request, 'post/signup.html', {'form': form})

def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = None
    return render(request, 'post/index.html', {'query': query, 'results': results})
