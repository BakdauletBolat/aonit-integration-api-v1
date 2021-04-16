from django.db import models


class EventGuest(models.Model):
    f_unic_id = models.CharField('Уникалныйидендификатор',max_length=255,null=True,blank=True)
    f_identifier = models.CharField('идентификатор',max_length=255,null=True,blank=True)
    f_name_resource = models.CharField('Ресурс контроллера',max_length=255,null=True,blank=True)
    f_name_ev = models.CharField('Наименование события',max_length=255,null=True,blank=True)
    f_name_obj = models.CharField('Имя обьекта',max_length=255,null=True,blank=True)
    f_name_subdiv = models.CharField('Наименование подразделения, если событие связано с сотрудником',max_length=255,null=True,blank=True)
    f_name_appoint = models.CharField('наименование должности, если событие связано с сотрудником',max_length=255,null=True,blank=True)
    f_date_ev = models.CharField('Дата',null=True,blank=True,max_length=255)
    f_time_ev = models.CharField('Время',null=True,blank=True,max_length=255)

    def __str__(self):

        return str(self.id)

class EventUser(models.Model):
    f_unic_id = models.CharField('Уникалныйидендификатор',max_length=255,null=True,blank=True)
    f_identifier = models.CharField('идентификатор',max_length=255,null=True,blank=True)
    f_name_resource = models.CharField('Ресурс контроллера',max_length=255,null=True,blank=True)
    f_name_ev = models.CharField('Наименование события',max_length=255,null=True,blank=True)
    f_name_obj = models.CharField('Имя обьекта',max_length=255,null=True,blank=True)
    f_name_subdiv = models.CharField('Наименование подразделения, если событие связано с сотрудником',max_length=255,null=True,blank=True)
    f_name_appoint = models.CharField('наименование должности, если событие связано с сотрудником',max_length=255,null=True,blank=True)
    f_fio = models.CharField('Фио',max_length=255,null=True,blank=True)
    f_date_ev = models.CharField('Дата',null=True,blank=True,max_length=255)
    f_time_ev = models.CharField('Время',null=True,blank=True,max_length=255)

    def __str__(self):

        return str(self.id)