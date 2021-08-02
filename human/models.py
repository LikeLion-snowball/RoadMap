from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Humanlog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]