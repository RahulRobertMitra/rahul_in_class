from django.db import models

class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title