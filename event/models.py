from django.db import models

class EventUser(models.Model):
    f_unic_id = models.CharField('ii',max_length=255,null=True,blank=True)
    f_areas_name = models.CharField('Вход/Выход',max_length=255,null=True,blank=True)
    f_identifier = models.CharField('идентификатор',max_length=255,null=True,blank=True)
    f_name_ev = models.CharField('Наименование события',max_length=255,null=True,blank=True)
    f_fio = models.CharField('Фио',max_length=255,null=True,blank=True)
    f_date_ev = models.CharField('Дата',null=True,blank=True,max_length=255)
    f_time_ev = models.CharField('Время',null=True,blank=True,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.f_fio)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Событий'
        ordering = ['f_name_ev']
