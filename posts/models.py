from django.db import models
from django.utils import timezone


class PostItem(models.Model):
    post_title = models.CharField(max_length=50)
    body = models.CharField(max_length=280)
    date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title
