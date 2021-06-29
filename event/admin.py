from django.contrib import admin
from .models import EventUser
# Register your models here.




class EventUserAdmin(admin.ModelAdmin):
    list_display = ('f_identifier','f_fio','f_date_ev','f_time_ev')



admin.site.register(EventUser,EventUserAdmin)




