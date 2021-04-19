from django.contrib import admin
from django.urls import path
from .views import index,loadStaffView

urlpatterns = [
    path('',index,name="main"),
    path('loadstaff/',loadStaffView,name="loadstaff"),
    path('admin/', admin.site.urls),
]
