from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

