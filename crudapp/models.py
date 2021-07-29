from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    body = models.TextField
    image = models.ImageField(upload_to='images/', default = "", null=True, blank=True)
    like_count = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username
    
