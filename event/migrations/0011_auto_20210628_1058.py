# Generated by Django 3.2 on 2021-06-28 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_eventuser_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventguest',
            name='f_name_appoint',
        ),
        migrations.RemoveField(
            model_name='eventguest',
            name='f_name_subdiv',
        ),
        migrations.RemoveField(
            model_name='eventguest',
            name='f_unic_id',
        ),
    ]
