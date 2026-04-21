from django.contrib import admin
from .models import Theme, Post

# Register your models here.

class ThemeAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "theme", "date_posted", "is_pinned")


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Post, PostAdmin)
