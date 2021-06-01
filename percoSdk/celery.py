import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'percoSdk.settings')

app = Celery('percoSdk')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'load and save events':{
        'task': 'event.tasks.loadUnitsandSave',
        'schedule':crontab(hour=23,minute=00)
    },
    'send req to Aonit':{
        'task': 'event.tasks.sendRequestToAonit',
        'schedule':crontab(hour=23,minute=50)
    } 
}
