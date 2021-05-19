from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index,loadUnitView,loadEventsView

urlpatterns = [
    path('',index,name="main"),
    path('loadunit/',loadUnitView,name="loadunit"),
    path('loadevents/',loadEventsView,name="loadevents"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



