# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Data(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    date_time = models.DateTimeField()

