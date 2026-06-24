from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Like, Comment


def home(request):
    return render(request, 'home.html')


def auth_gate(request):
    return render(request, 'auth_gate.html')


from .forms import StyledUserCreationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = StyledUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = StyledUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def post_list(request):
    q = request.GET.get('q', '')
    posts = Post.objects.all().order_by('-id')
    if q:
        posts = posts.filter(title__icontains=q)
    categories = Category.objects.all()
    return render(request, 'post_list.html', {
        'posts': posts,
        'categories': categories,
        'q': q,
    })


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.all()
    return render(request, 'post_detail.html', {
        'post': post,
        'categories': categories,
    })


@login_required
def category_posts(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-id')
    categories = Category.objects.all()
    return render(request, 'post_list.html', {
        'posts': posts,
        'categories': categories,
        'q': '',
    })


@login_required
def about(request):
    categories = Category.objects.all()
    return render(request, 'about.html', {'categories': categories})


@login_required
def contact(request):
    categories = Category.objects.all()
    return render(request, 'contact.html', {'categories': categories})

@login_required
def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.create(post=post)
    return redirect('post_detail', pk=pk)


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, content=content)
    return redirect('post_detail', pk=pk)