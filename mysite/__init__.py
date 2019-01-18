# from .tasks import app as celery_app
#
# __all__ = ['celery_app']

from __future__ import absolute_import

from .tasks import app as celery_app

"""
콘솔로 radis 실행 
$ /Users/uiandwe/Downloads/redis-stable/src/radis-server 
$ /Users/uiandwe/Downloads/redis-stable/src/radis-client
> ping 
으로 서버 실행 확인 

celery worker 실행 $ celery -A /Users/uiandwe/PycharmProjects/django_tutorial/mysite  worker -l info
- worker 실행시 실행 가능한 task 목록이 있음.
        app.conf.beat_schedule = {
            'add-every-5-seconds': {
                'task': 'mysite.tasks.add',
                'schedule': 5.0,  
                'args': (16, 16)
            },
        }


celery beat 실행 $ celery -A /Users/uiandwe/PycharmProjects/django_tutorial/mysite beat -l info


celery의 task에서 5초마다 rabbitMQ로 메시지 전달

메시지를 받는것은 /Users/uiandwe/PycharmProjects/django_tutorial/mq_recevie.py

python3 /Users/uiandwe/PycharmProjects/django_tutorial/mq_recevie.py 
로 해당 메시지를 확인 가능 해당 파일로 메시지 처리를 담당



"""

