from django.db import models
from django.conf import settings

# Create your models here.
class Video(models.Model):
    writer = models.ForeignKey('user.meokda_user', on_delete = models.CASCADE, verbose_name = '작성자')
    title = models.CharField(max_length = 128, verbose_name = '제목')
    file = models.FileField()
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = '등록시간')
    updated_at = models.DateTimeField(auto_now = True)