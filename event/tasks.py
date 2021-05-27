from celery import shared_task
from .models import EventUser,Unit,TestDB
from django.core.exceptions import ObjectDoesNotExist
import string,random

@shared_task
def test812():
    
    test820 = TestDB.objects.create(
        name='im created in 8 22'
    )
    test820.save()



