from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Theme
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blog_index(request):
    pinned = Post.objects.filter(is_pinned=True)
    recent = Post.objects.filter(is_pinned=False).order_by("-date_posted")[:6]
    context = {
        "pinned": pinned,
        "recent": recent,
    }
    return render(request, "blog/index.html", context)

def blog_theme(request, theme):
    posts = Post.objects.filter(theme__name__icontains=theme).order_by("-date_posted")
    context = {
        "theme": theme,
        "posts": posts,
    }
    return render(request, "blog/theme.html", context)

def theme_list(request):
    themes = Theme.objects.all().order_by("name")
    context = {
        "themes": themes,
    }
    return render(request, "blog/theme_list.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "blog/detail.html", context)

def all_posts(request):
    posts = Post.objects.all().order_by("-date_posted")
    p = Paginator(posts, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "blog/the_feed.html", context)

def about(request):
    return render(request, "blog/about.html")

def search(request):
    query = request.GET.get("q", "")
    results = []
    error = None

    if query:
        if len(query) > 50:
            error = "Search query cannot exceed 50 characters."
        else:
            results = Post.objects.filter(
                title__icontains=query
            ) | Post.objects.filter(
                content__icontains=query
            ) | Post.objects.filter(
                theme__name__icontains=query
            )
            results = results.distinct().order_by("-date_posted")

    context = {
        "query": query,
        "results": results,
        "error": error,
    }
    return render(request, "blog/search.html", context)

