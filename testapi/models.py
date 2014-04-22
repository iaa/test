# -*- coding: utf-8 -*-
from django.db import models


class SmsLog(models.Model):
    level = models.CharField(max_length=200)
    message = models.TextField()
    info = models.TextField()
    timestamp = models.DateTimeField()
