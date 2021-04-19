from django.contrib import admin
from .models import EventUser, User
# Register your models here.


class EventUserAdmin(admin.ModelAdmin):
    list_filter = ('f_name_subdiv','f_name_resource')
    list_display = ('f_identifier','f_name_subdiv','f_fio','f_date_ev','f_time_ev')

admin.site.register(EventUser,EventUserAdmin)


admin.site.register(User)