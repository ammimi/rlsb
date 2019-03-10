from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rlsb.settings')

app = Celery('rlsb')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

BROKER_URL = 'redis://localhost:6379/0'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_ENABLE_UTC = False

CELERYD_FORCE_EXECV = True

CELERYD_CONCURRENCY = 5

CELERY_ACKS_LATE = True

CELERYD_MAX_TASKS_PER_CHILD = 100

CELERYD_TASK_TIME_LIMIT = 60 * 5


app.conf.ONCE = {
    'backend': 'celery_once.backends.Redis',
    'settings': {
        'url': 'redis://localhost:6379/2',
        'default_timeout': 60 * 5
    }
}



CELERYBEAT_SCHEDULE = {
    'add-every-3-seconds': {
        'task': 'system.tasks.add',
        # 'schedule': crontab(minute=u'40', hour=u'17',),
        'schedule': timedelta(seconds=3),
        'args': (16, 16)
    },
    'send-every-2-seconds': {
        'task': 'system.tasks.sendFrameWithCam',
        # 'schedule': crontab(minute=u'40', hour=u'17',),
        'schedule': timedelta(seconds=2),
        'args': ()
    },
}

