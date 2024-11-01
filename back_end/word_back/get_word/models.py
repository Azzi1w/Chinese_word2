from django.db import models
from datetime import datetime


class Words(models.Model):
    chine = models.CharField(max_length=300)
    pinyin = models.CharField(max_length=300)
    translate = models.CharField(max_length=300)
    date_str =  models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.chine