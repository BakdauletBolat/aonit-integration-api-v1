from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from event.models import EventGuest,EventUser
def index(request):
    from .utils import loadStaff,loadEvents
    events = loadEvents()
    for event in events:
        if event['f_fio'] != "":
            try:
                eventD = EventUser.objects.get(f_unic_id=event['f_unic_id'])
            except ObjectDoesNotExist:
                eventD = EventUser(
                    f_name_resource = event['f_name_resource'],
                    f_name_ev = event['f_name_ev'],
                    f_name_obj = event['f_name_obj'],
                    f_name_subdiv = event['f_name_subdiv'],
                    f_name_appoint = event['f_name_appoint'],
                    f_fio = event['f_fio'],
                    f_date_ev = event['f_date_ev'],
                    f_time_ev = event['f_time_ev'],
                    f_identifier = event['f_identifier'],
                    f_unic_id = event['f_unic_id']
                )
                eventD.save()
        else:
            pass
    return render(request,'main/index.html')

