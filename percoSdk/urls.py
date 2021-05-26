from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from .views import index,loadUnitView,loadEventsView
from event.models import EventUser

def delete_events(request):
    events = EventUser.objects.all()
    for event in events:
        event.delete()

    return redirect('/')


urlpatterns = [
    # path('',index,name="main"),
    path('delete-events/', delete_events),
    path('loadunit/',loadUnitView,name="loadunit"),
    path('loadevents/',loadEventsView,name="loadevents"),
    path('', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



