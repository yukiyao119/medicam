# Generated by Django 3.0.4 on 2020-03-22 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_selfcertificationquestion_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='fcm_token',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_notified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='notify',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='notify_interval',
            field=models.DurationField(blank=True, default=datetime.timedelta(seconds=21600), null=True, verbose_name='notify me no more than once every'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='quiet_time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='end of quiet hours'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='quiet_time_start',
            field=models.TimeField(blank=True, null=True, verbose_name='start of quiet hours'),
        ),
    ]