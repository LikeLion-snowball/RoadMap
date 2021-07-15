# from RoadMap.user.views import portfolio
# from django.db import models

# from django.db import models
# # from account.models import User

# class Portfolio(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     isPrivate = models.BooleanField(default=False)

# class Projects(models.Model):
#     portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
#     project_name = models.CharField(max_length=50)
#     project_start = models.DateField()
#     project_end = models.DateField()
#     project_github = models.URLField()

# class Activities(models.Model):
#     portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
#     activity_name = models.CharField(max_length=50)
#     activity_start = models.DateField()
#     activity_end = models.DateField()
