from django.contrib import admin
from .models import Humanlog, Comment


# Register your models here.
admin.site.register(Humanlog)
admin.site.register(Comment)