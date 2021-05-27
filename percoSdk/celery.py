import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'percoSdk.settings')

app = Celery('percoSdk')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'test in 8 12':{
        'task': 'event.tasks.test812',
        'schedule':crontab(hour=20,minute=22)
    },
    'test in 8 15':{
        'task': 'event.tasks.test815',
        'schedule':crontab(hour=20,minute=23)
    },
    'test in 8 18':{
        'task': 'event.tasks.test818',
        'schedule':crontab(hour=20,minute=24)
    },
    'test in 8 20':{
        'task': 'event.tasks.test820',
        'schedule':crontab(hour=20,minute=25)
    }
}
