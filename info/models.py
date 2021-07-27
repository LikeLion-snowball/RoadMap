from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recruit(models.Model):
    corp = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    link = models.URLField()
    end_date = models.DateField(null=True, blank=True)
    end_date_str = models.CharField(max_length=20, null=True, blank=True)
    career = models.CharField(max_length=20)
    academic = models.CharField(max_length=20)
    type = models.CharField(max_length=20, null=True, blank=True)
    area = models.CharField(max_length=20)
    scrap = models.ManyToManyField(User, related_name="recruits", through='Scrap')
    scrap_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.corp

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recruit = models.ForeignKey(Recruit, related_name="scraps", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)