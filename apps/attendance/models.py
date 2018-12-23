from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class AttendanceInfo(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='姓名')
    attendancetime = models.DateTimeField(auto_now_add=True,verbose_name='考勤时间')
    image = models.ImageField( upload_to="attendance/%Y/%m", null=True, blank=True,verbose_name="考勤图片")

    def __str__(self):
        return self.person.name

    class Meta:
        verbose_name = '考勤信息'
        verbose_name_plural = verbose_name
        ordering = ['id']
