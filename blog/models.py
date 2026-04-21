from django.db import models

# Create your models here.

class Theme(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    theme = models.ForeignKey(Theme, related_name="posts", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50] + "..."
        return self.title
    

