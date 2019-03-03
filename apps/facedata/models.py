from django.db import models

from django.utils import timezone
from system.models import Structure
import datetime
# Create your models here.
import imghdr

class FaceData(models.Model):
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")),
                              default="male", verbose_name="性别")
    mobile = models.CharField(max_length=11, default="", verbose_name="手机号码")
    joindate = models.DateField(verbose_name="入职日期",default=datetime.date.today())
    department = models.ForeignKey(Structure, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="部门")

    face_id = models.CharField(max_length=30, blank=True,null=True,unique=True, verbose_name="人脸样本ID")  # unique=True, 这个字段在表中必须有唯一值.
    face_name = models.CharField(max_length=30, verbose_name="人脸拼音名称")
    face_cname = models.CharField(max_length=30, verbose_name="人脸中文名称")
    face_image = models.ImageField( upload_to="facedata/%Y/%m", null=True, blank=True,verbose_name="人脸图片")
    ifsync = models.BooleanField(verbose_name='是否同步数据',default=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人脸样本信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

