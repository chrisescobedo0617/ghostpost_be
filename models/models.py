from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    POST_CHOICES = ((True, 'Boast'), (False, 'Roast'))

    post_type = models.BooleanField(choices=POST_CHOICES)
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    @property
    def total_votes(self):
        return self.upvotes - self.downvotes
