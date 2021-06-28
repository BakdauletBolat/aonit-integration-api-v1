from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from event.models import EventUser, Unit
from itertools import islice
from datetime import datetime
def index(request):

    return render(request,'main/index.html')


def loadUnitView(request):
    from .utils import loadUnits
    units = loadUnits()
    for unit in units:

        try:
            unitM = Unit.objects.get(id_internal=unit['id_internal'])
        except ObjectDoesNotExist:
            unitM = Unit(
                displayname = unit['displayname'],
                id_internal = unit['id_internal'],
                id_parent = unit['id_parent'],
                bin = 1
            )
            unitM.save()

    return redirect('main')

def loadTestEventsView(request):
    from .utils import loadTest
    eventsCache = EventUser.objects.filter(created_at__date=datetime.today()).delete()
    events = loadTest()
    batch_size = len(events)
    objs = (EventUser(
        f_areas_name=events[i]['f_areas_name'],
        f_identifier=events[i]['f_identifier'],
        f_name_ev=events[i]['f_name_ev'],
        f_fio=events[i]['f_fio'],
        f_date_ev=events[i]['f_date_ev'],
        f_time_ev=events[i]['f_time_ev'],
    ) for i in range(batch_size))
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        EventUser.objects.bulk_create(batch, batch_size)

    return redirect('home')


def loadEventsView(request):
    from .utils import loadEvents
    events = loadEvents()
    for event in events:
        if event['f_fio'] != "":
            try:
                eventD = EventUser.objects.get(f_unic_id=event['f_unic_id'])
            except ObjectDoesNotExist:
                try:
                    eventD = EventUser(
                        f_unic_id = event['f_unic_id'],
                        f_areas_name = event['f_areas_name'],
                        f_identifier = event['f_identifier'],
                        f_name_ev = event['f_name_ev'],
                        f_fio = event['f_fio'],
                        f_date_ev = event['f_date_ev'],
                        f_time_ev = event['f_time_ev'],
                    )
                    eventD.save()
                except ObjectDoesNotExist:
                    pass
        else:
            pass
    return redirect('home')