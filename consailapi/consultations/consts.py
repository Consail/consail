from datetime import timedelta

from django.db import models


class ReservationDuration(timedelta, models.Choices):
    FIFTEEN_MINUTES = 0, 900, "15min"
    HALF_HOUR = 0, 1800, "30min"
    FORTY_FIVE_MINUTES = 0, 2700, "45min"
    HOUR = 0, 3600, "1h"


class ReservationDurationInt(models.IntegerChoices):
    FIFTEEN_MINUTES = 15
    HALF_HOUR = 30
    FORTY_FIVE_MINUTES = 45
    HOUR = 60
