from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    body = models.TextField
    image = models.ImageField(upload_to='images/', default = "", null=True, blank=True)
    like_count = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username
    
