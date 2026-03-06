from django.db import models
from django.utils import timezone

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)