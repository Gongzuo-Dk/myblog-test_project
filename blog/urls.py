from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("theme/<theme>/", views.blog_theme, name="blog_theme"),
    path("themes/", views.theme_list, name="theme_list" ),
    path("about/", views.about, name="about"),
    path("posts/", views.all_posts, name="feed"),
    path("search/", views.search, name="search"),
]