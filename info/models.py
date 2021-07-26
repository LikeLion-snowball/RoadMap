from django.db import models

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
    
    def __str__(self):
        return self.corp