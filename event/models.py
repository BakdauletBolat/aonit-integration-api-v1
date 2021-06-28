from django.db import models


class Unit(models.Model):

    id_internal = models.CharField('Уникалный id',max_length=255,null=True,blank=True)
    id_parent = models.CharField('Уникалный id парента',max_length=255,null=True,blank=True)
    displayname = models.CharField('Имя',max_length=255,null=True,blank=True)
    bin = models.CharField('БИН',max_length=255,null=True,blank=True)

    def __str__(self):

        return f'Имя: {self.displayname},  Id: {self.id_internal}, Бинн: {self.bin} Parent_id: {self.id_parent}'

    class Meta:

        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделений'
        ordering = ['displayname']


class EventGuest(models.Model):
    f_identifier = models.CharField('идентификатор',max_length=255,null=True,blank=True)
    f_name_resource = models.CharField('Ресурс контроллера',max_length=255,null=True,blank=True)
    f_name_ev = models.CharField('Наименование события',max_length=255,null=True,blank=True)
    f_name_obj = models.CharField('Имя обьекта',max_length=255,null=True,blank=True)
    f_date_ev = models.CharField('Дата',null=True,blank=True,max_length=255)
    f_time_ev = models.CharField('Время',null=True,blank=True,max_length=255)

    def __str__(self):

        return str(self.id)




class EventUser(models.Model):
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

class TestDB(models.Model):

    name = models.CharField(max_length=255)