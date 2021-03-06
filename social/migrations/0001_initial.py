# Generated by Django 2.2.16 on 2020-10-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='滑动ID')),
                ('sid', models.IntegerField(verbose_name='被滑动ID')),
                ('stype', models.CharField(choices=[('like', '喜欢'), ('superlike', '超级喜欢'), ('dislike', '不喜欢')], max_length=25, verbose_name='滑动类型')),
                ('stime', models.DateTimeField(auto_now_add=True, verbose_name='滑动时间')),
            ],
            options={
                'unique_together': {('uid', 'sid')},
            },
        ),
    ]
