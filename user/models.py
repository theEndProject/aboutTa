import datetime

from django.db import models

# Create your models here.
from vip.models import Vip


class User(models.Model):
    '''User模型'''
    GENDERS = (
        ('male', '男性'),
        ('female', '女性'),
        # ('xxx', '保密') 交友网站非男及女，不能保密
    )
    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('西安', '西安'),
        ('沈阳', '沈阳'),
        ('武汉', '武汉'),
        ('成都', '成都'),
    )
    phonenum = models.CharField(verbose_name='手机号', max_length=16, unique=True)
    nickname = models.CharField(verbose_name='昵称', max_length=25, db_index=True)
    gender = models.CharField(verbose_name='性别', max_length=25, choices=GENDERS, default='male')
    birthday = models.DateField(verbose_name='出生日', default='2002-01-01')
    avatar = models.CharField(verbose_name='个人形象', max_length=255)
    location = models.CharField(verbose_name='常居地', max_length=25, choices=LOCATIONS, default='上海')

    vip_id = models.IntegerField(verbose_name='用户购买的VIP的ID', default=1)
    vip_end = models.DateTimeField(default='3000-12-31', verbose_name='VIP过期时间')

    @property
    # 建立与profile的一对一关系
    def profile(self):
        '''当前用户对应的Profile'''
        if not hasattr(self, '_profile'):  # 判断用户的交友资料里面是否没有对应的id
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        # get_or_create获取或者创建，先获取后创建，如果获取不到就创建一下，所以都要添加一下默认值
        # get_or_create 有两个返回值
        # 单独的下划线可以占位，可以接受到后面的返回值
        return self._profile

    @property
    def vip(self):
        '''当前用户对应的VIP'''
        # 检查当前会员是否过期
        now = datetime.datetime.now()
        if now >= self.vip_end:
            self.set_vip(1)  # 强制设置成非会员
        if not hasattr(self, '_vip'):
            self._vip = Vip.objects.get(id=self.vip_id)
        return self._vip

    '''
        Python中的属性操作
            setattr(obj,name,value) 修改属性值
            getattr(obj,name)       获取属性值
            delattr(obj,name)       删除属性值
            hasattr(obj,name)       判断有没有该属性值
    '''

    def set_vip(self, vip_id):
        '''设置当前用户的VIP'''
        vip = Vip.objects.get(id=vip_id)
        self.vip_id = vip_id
        self.vip_end = datetime.datetime.now() + datetime.timedelta(vip.duration)  # 当前时间加上vip时间
        self._vip = vip
        self.save()

    def to_dict(self):
        # 很low，很多地方用到会封装一下
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'gender': self.gender,
            'birthday': str(self.birthday),  # DateField需要转义
            'avatar': self.avatar,
            'location': self.location,
        }


class Profile(models.Model):
    '''用户的交友资料'''
    dating_location = models.CharField(verbose_name='目标城市', max_length=25, choices=User.LOCATIONS, default='上海')
    dating_gender = models.CharField(verbose_name='匹配性别', max_length=25, choices=User.GENDERS, default='female')

    min_distance = models.IntegerField(verbose_name='最小查找范围', default=1)
    max_distance = models.IntegerField(verbose_name='最大查找范围', default=50)

    min_dating_age = models.IntegerField(verbose_name='最小交友年龄', default=18)
    max_dating_age = models.IntegerField(verbose_name='最大交友年龄', default=50)

    vibration = models.BooleanField(verbose_name='开启震动', default=True)
    only_matched = models.BooleanField(verbose_name='不让陌生人看我的相册', default=True)
    auto_play = models.BooleanField(verbose_name='自动播放视频', default=True)

    def to_dict(self):
        # 很low，很多地方用到会封装一下
        return {
            'id': self.id,
            'dating_location': self.dating_location,
            'dating_gender': self.dating_gender,
            'min_distance': self.min_distance,
            'max_distance': self.max_distance,
            'min_dating_age': self.min_dating_age,
            'max_dating_age': self.max_dating_age,
            'vibration': self.vibration,
            'only_matched': self.only_matched,
            'auto_play': self.auto_play,
        }
