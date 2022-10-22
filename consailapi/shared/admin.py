from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django_celery_beat.models import (
    ClockedSchedule,
    CrontabSchedule,
    IntervalSchedule,
    PeriodicTask,
    SolarSchedule,
)
from rest_framework.authtoken.models import TokenProxy

admin.site.unregister(ClockedSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(SolarSchedule)
admin.site.unregister(TokenProxy)
admin.site.unregister(Group)
admin.site.unregister(Site)
