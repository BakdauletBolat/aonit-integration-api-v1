from celery import shared_task
from .models import EventUser,Unit
from django.core.exceptions import ObjectDoesNotExist
import string,random

@shared_task
def getEventForDay():
    from percoSdk.utils import loadEvents

    events = loadEvents()
    
    for event in events:
        if event['f_fio'] != "":
            try:
                eventD = EventUser.objects.get(f_unic_id=event['f_unic_id'])
        
            except ObjectDoesNotExist:

                try:
                    unit = Unit.objects.get(id_internal=event['f_subdiv_id_internal'])
                    eventD = EventUser(
                        f_unic_id = event['f_unic_id'],
                        f_areas_name = event['f_areas_name'],
                        f_identifier = event['f_identifier'],
                        f_name_ev = event['f_name_ev'],
                        f_name_subdiv = unit.displayname or unit,
                        f_subdiv_id_internal = unit.id_internal or unit,
                        f_fio = event['f_fio'],
                        f_date_ev = event['f_date_ev'],
                        f_time_ev = event['f_time_ev'],
                        bin = unit.bin or unit
                    )
                    eventD.save()
                except ObjectDoesNotExist:
                    
                    pass
                
        else:
            pass



