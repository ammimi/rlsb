from django.db import models

# Create your models here.


class FaceData(models.Model):

    face_id = models.CharField(max_length=30, unique=True, verbose_name="人脸样本ID")  # unique=True, 这个字段在表中必须有唯一值.
    face_name = models.CharField(max_length=30, verbose_name="人脸拼音名称")
    face_name = models.CharField(max_length=30, verbose_name="人脸中文名称")
    face_image_url = models.URLField(max_length=50, null=True, blank=True, verbose_name="人脸样本图片Url地址")

    def __str__(self):
        return self.face_name

    class Meta:
        verbose_name = '人脸样本信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

