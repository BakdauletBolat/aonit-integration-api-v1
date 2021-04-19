from django.contrib import admin
from django.urls import path
from .views import index,loadUnitView,loadEventsView

urlpatterns = [
    path('',index,name="main"),
    path('loadunit/',loadUnitView,name="loadunit"),
    path('loadevents/',loadEventsView,name="loadevents"),
    path('admin/', admin.site.urls),
]
