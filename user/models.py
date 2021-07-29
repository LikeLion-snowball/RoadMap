from django.conf import settings
from django.db import models

class Project(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    project_start = models.DateField()
    project_end = models.DateField()
    project_detail = models.CharField("사용 언어나 프레임워크", max_length=50)
    project_github = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.project_name

class Activity(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=50)
    activity_start = models.DateField()
    activity_end = models.DateField()

    def __str__(self):
        return self.activity_name
