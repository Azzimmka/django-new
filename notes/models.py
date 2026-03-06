from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)