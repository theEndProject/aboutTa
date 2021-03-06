import os

from celery import Celery
from tasks import config
'''
    Celery 的使用场景
        发短信
        发送邮件
        定时任务
        图片的压缩
        视频处理
        复杂算法处理
'''
# 因为发短信太慢，所以用异步Celery

# 要加载django首先要加载django的settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aboutTa.settings')

# Celery要独立运行
celery_app = Celery('tasks')
celery_app.config_from_object(config)  # 从一个对象的位置加载配置
celery_app.autodiscover_tasks()  # 自动发现django里面的任务
