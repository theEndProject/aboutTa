# Generated by Django 2.2.16 on 2020-10-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dating_gender',
            field=models.CharField(choices=[('male', '男性'), ('female', '女性')], default='female', max_length=25, verbose_name='匹配性别'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dating_location',
            field=models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('西安', '西安'), ('沈阳', '沈阳'), ('武汉', '武汉'), ('成都', '成都')], default='上海', max_length=25, verbose_name='目标城市'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', '男性'), ('female', '女性')], default='male', max_length=25, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('西安', '西安'), ('沈阳', '沈阳'), ('武汉', '武汉'), ('成都', '成都')], default='上海', max_length=25, verbose_name='常居地'),
        ),
    ]
