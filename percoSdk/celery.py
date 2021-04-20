import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'percoSdk.settings')

app = Celery('percoSdk')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'getEventData':{
        'task': 'event.tasks.getEventForDay',
        'schedule':60.0
    }
}
