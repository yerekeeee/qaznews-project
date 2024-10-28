from django.shortcuts import render, get_object_or_404, redirect
from .models import Tag, Post
from django.core.paginator import Paginator
from django.db.models import Q

from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomAuthenticationForm, TagForm, PostForm


def home_page(request):
    primary_posts = Post.objects.all().order_by('-created_at')[:1]
    last_posts =  Post.objects.all().order_by('-created_at')[:6]
    tags = Tag.objects.all()[:3]
    context = {
        'primary_posts': primary_posts,
        'last_posts': last_posts,
        'tags': tags
    }
    return render(request, "./client/home.html", context)

def all_news_page(request):
    tags = Tag.objects.all()
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'tags': tags,
        'posts': posts
    }
    return render(request, "./client/all-news.html", context)

def news_detail_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.all()
    last_posts = Post.objects.all().order_by('-created_at')[:3]
    context = {
        'post': post,
        'tags': tags,
        'last_posts': last_posts
    }
    return render(request, "./client/news-detail.html", context)

def search_page(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, "./client/search.html", context)

def search_results_page(request):
    query = request.GET.get('q', '').strip()
    post_list = Post.objects.filter(
        Q(title__icontains=query)
    ) | Post.objects.filter(
        Q(description__icontains=query)
    )
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    tags = Tag.objects.all()
    context = {
        'tags': tags,
        'posts': posts,
        'query': query
    }
    return render(request, "./client/search-results.html", context)

def tags_news_page(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    post_list = Post.objects.filter(tag=tag)
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    tags = Tag.objects.all()
    context = {
        'tag': tag,
        'posts': posts,
        'tags': tags
    }
    return render(request, "./client/tags-news.html", context)


def admin_login_page(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard_page')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "./admin/admin-login.html", context)

def admin_dashboard_page(request):
    return render(request, "./admin/admin-dashboard.html")

def admin_logout(request):
    logout(request)
    return redirect("home_page")


def admin_tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, "./admin/admin-tags-list.html", context)

def admin_tags_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_tags_list')
    else:
        form = TagForm()
    context = {
        'form': form
    }
    return render(request, "./admin/admin-tags-create.html", context)


def admin_tags_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('admin_tags_list')
    else:
        form = TagForm(instance=tag)
    context = {
        'form': form
    }
    return render(request, "./admin/admin-tags-update.html", context)


def admin_tags_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("admin_tags_list")
    context = {
        'tag': tag
    }
    return render(request, "./admin/admin-tags-delete.html", context)

def admin_news_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "./admin/admin-news-list.html", context)

def admin_news_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_news_list')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, "./admin/admin-news-create.html", context)


def admin_news_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('admin_news_list')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, "./admin/admin-news-update.html", context)


def admin_news_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("admin_news_list")
    context = {
        'post': post
    }
    return render(request, "./admin/admin-news-delete.html", context)