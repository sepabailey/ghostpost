from django.db import models
from django.utils import timezone


class PostItem(models.Model):
    post_title = models.CharField(max_length=50)
    body = models.CharField(max_length=280)
    date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    results = models.IntegerField(default=0)
    # Matt helped with boast and roast concept
    boast_or_roast = models.BooleanField(
        default=False, help_text="Boast if checked")

    def __str__(self):
        return self.post_title
