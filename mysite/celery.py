# http://wangin9.tistory.com/entry/celery
from __future__ import absolute_import

import os

from celery import Celery

# Django의 세팅 모듈을 Celery의 기본으로 사용하도록 등록합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# 문자열로 등록한 이유는 Celery Worker가 자식 프로세스에게 configuration object를 직렬화하지 않아도 된다는것 때문
# namespace = 'CELERY'는 모든 celery 관련한 configuration key가 'CELERY_' 로 시작해야함을 의미함
app.config_from_object('django.conf:settings', namespace='CELERY')

# task 모듈을 모든 등록된 Django App configs에서 load 함
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


from celery.schedules import crontab

app.conf.beat_schedule = {
    'add-every-minute-contrab': {
        'task': 'multiply_two_numbers',
        'schedule': crontab(),  # 1분마다
        'args': (16, 16),
    },
    'add-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0,  # 5초마다
        'args': (16, 16)
    },
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,  # 30초마다
        'args': (16, 16)
    },
}
