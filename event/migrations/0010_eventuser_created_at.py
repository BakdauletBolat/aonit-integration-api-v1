# Generated by Django 3.2 on 2021-06-01 06:37

from django.db import migrations, models
from datetime import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20210601_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.now()),
            preserve_default=False,
        ),
    ]