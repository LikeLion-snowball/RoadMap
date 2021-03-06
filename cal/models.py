from django.db import models
from django.urls import reverse
from django.conf import settings

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    start_time = models.DateTimeField("시작시간")
    end_time = models.DateTimeField("마감시간")
    title = models.CharField("이벤트 이름", max_length=50)
    description = models.TextField("상세")

    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('eventedit', args=(self.user.id, self.id))
        return f'<a href="{url}"> {self.title} </a>'