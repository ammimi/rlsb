from django.db import models
from mptt.models import MPTTModel
from django.contrib.auth.models import AbstractUser


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")  # unique=True, 这个字段在表中必须有唯一值.
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="编码")
    url = models.CharField(max_length=128, unique=True, null=True, blank=True)
    number = models.FloatField(null=True, blank=True, verbose_name="编号")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['number']

    @classmethod
    def get_menu_by_request_url(cls, url):
        try:
            return dict(menu=Menu.objects.get(url=url))
        except:
            None


class Role(models.Model):
    """
    角色：用于权限绑定
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色")
    permissions = models.ManyToManyField("menu", blank=True, verbose_name="URL授权")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")


class Structure(MPTTModel):
    """
    组织架构
    """
    type_choices = (("unit", "单位"), ("department", "部门"))
    name = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choices, default="department", verbose_name="类型")
    client_name = models.CharField(max_length=30, blank=True,null=True, verbose_name="客户拼音名称")
    client_cname = models.CharField(max_length=30, blank=True,null=True, verbose_name="客户中文名称")
    client_id = models.CharField(max_length=30, blank=True,null=True,unique=True, verbose_name="客户标识ID")
    client_secret = models.CharField(max_length=30, blank=True,null=True,verbose_name="客户密钥")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父类架构",related_name='children')

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        super(Structure, self).save(*args, **kwargs)
        Structure.objects.rebuild()

class CameraSet(models.Model):
    usercam = models.CharField(max_length=20,verbose_name='摄像头用户名')
    pwdcam = models.CharField(max_length=20,verbose_name='摄像头密码')
    ipcam = models.GenericIPAddressField(verbose_name='摄像头IP')
    portcam = models.IntegerField(verbose_name='摄像头端口')
    webcamid = models.CharField(max_length=10,verbose_name='摄像头ID')
    company = models.ForeignKey(Structure,verbose_name='公司信息',on_delete=models.CASCADE)

class WorktimeSet(models.Model):
    uptime = models.TimeField(verbose_name='上班时间')
    downtime = models.TimeField(verbose_name='下班时间')
    company = models.OneToOneField(Structure, verbose_name='公司信息',on_delete=models.CASCADE)


class UserProfile(AbstractUser):
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")),
                              default="male", verbose_name="性别")
    mobile = models.CharField(max_length=11, default="", verbose_name="手机号码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg",
                              max_length=100, null=True, blank=True)
    department = models.ForeignKey("Structure", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="部门")
    post = models.CharField(max_length=50, null=True, blank=True, verbose_name="职位")
    superior = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="上级主管")
    roles = models.ManyToManyField("role", verbose_name="角色", blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class SystemSetup(models.Model):
    loginTitle = models.CharField(max_length=20, null=True, blank=True, verbose_name='登录标题')
    mainTitle = models.CharField(max_length=20, null=True, blank=True, verbose_name='系统标题')
    headTitle = models.CharField(max_length=20, null=True, blank=True, verbose_name='浏览器标题')
    copyright = models.CharField(max_length=100, null=True, blank=True, verbose_name='底部版权信息')
    url = models.CharField(max_length=50, null=True, blank=True, verbose_name='系统URL地址')


    def __str__(self):
        return self.loginTitle

    class Meta:
        verbose_name = "系统设置"
        verbose_name_plural = verbose_name

    @classmethod
    def getSystemSetupLastData(self):
        return dict(system_setup=SystemSetup.objects.last())
