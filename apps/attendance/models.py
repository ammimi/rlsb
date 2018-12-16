from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class AttendanceInfo(models.Model):
    attendancetime = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(User)  # unique=True, 这个字段在表中必须有唯一值.
    image = models.ImageField( verbose_name="考勤图片")

    def __str__(self):
        return self.person.name

    class Meta:
        verbose_name = '考勤信息'
        verbose_name_plural = verbose_name
        ordering = ['id']
