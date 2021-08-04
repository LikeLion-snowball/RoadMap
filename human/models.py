from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Humanlog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    body = models.TextField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post',through='Like', blank=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Humanlog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Humanlog, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
