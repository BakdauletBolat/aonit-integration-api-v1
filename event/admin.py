from django.contrib import admin
from .models import EventUser, TestDB,Unit
# Register your models here.


class EventUserAdmin(admin.ModelAdmin):
    list_filter = ('f_name_subdiv',)
    list_display = ('f_identifier','f_name_subdiv','f_fio','f_date_ev','f_time_ev','bin')



admin.site.register(EventUser,EventUserAdmin)



class UnitAdmin(admin.ModelAdmin):
    list_filter = ('id_parent',)
    list_display = ('id_internal','id_parent','displayname','bin')

admin.site.register(Unit,UnitAdmin)
admin.site.register(TestDB)
