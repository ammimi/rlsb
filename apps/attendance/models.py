from django.db import models
from django.contrib.auth import get_user_model
from facedata.models import FaceData
User = get_user_model()

# Create your models here.
class AttendanceInfo(models.Model):
    facedata  = models.ForeignKey(FaceData,on_delete=models.CASCADE,verbose_name='人脸信息')
    recorded_datetime = models.DateTimeField(blank=True,null=True,verbose_name='考勤时间')
    image = models.ImageField( upload_to="attendance/%Y/%m", null=True, blank=True,verbose_name="考勤图片")
    recorded_img_url = models.CharField(max_length=100, null=True, blank=True, verbose_name="考勤图片")

    def __str__(self):
        return self.facedata.face_cname

    class Meta:
        verbose_name = '考勤信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

class ImageTmp(models.Model):
    image = models.ImageField( upload_to="attendancetmp/%Y/%m", null=True, blank=True,verbose_name="考勤图片")