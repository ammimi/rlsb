from django.db import models
from django.contrib.auth import get_user_model
from facedata.models import FaceData
import datetime
User = get_user_model()

# Create your models here.
class AttendanceInfo(models.Model):
    type_choices = (("上班考勤", "上班考勤"), ("下班考勤", "下班考勤"))

    facedata  = models.ForeignKey(FaceData,on_delete=models.CASCADE,verbose_name='人脸信息')
    recorded_datetime = models.DateTimeField(blank=True,null=True,verbose_name='考勤时间')
    state = models.CharField(choices=type_choices,max_length=10,verbose_name='考勤状态',blank=True,null=True)
    image = models.ImageField( upload_to="attendance/%Y/%m", null=True, blank=True,verbose_name="考勤图片")
    recorded_img_url = models.CharField(max_length=100, null=True, blank=True, verbose_name="考勤图片")

    def __str__(self):
        return self.facedata.face_cname

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        records =  AttendanceInfo.objects.filter(facedata=self.facedata,recorded_datetime__gte=datetime.datetime.now().date()).order_by('id')
        num = len(records)
        if num == 0 :#每天第一条记录 state = up
            self.state = '上班考勤'
            super(AttendanceInfo,self).save()
        if num == 1 :##第二条记录 state = down
            self.state = '下班考勤'
            super(AttendanceInfo, self).save()
        if num == 2 : #超过两条，更新
            AttendanceInfo.objects.filter(id=records[1].id).update(recorded_datetime=datetime.datetime.now())









    class Meta:
        verbose_name = '考勤信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

class ImageTmp(models.Model):
    image = models.ImageField( upload_to="attendancetmp/%Y/%m", null=True, blank=True,verbose_name="考勤图片")