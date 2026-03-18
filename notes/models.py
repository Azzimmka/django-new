from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title or f"Note #{self.pk}"

    class Meta:
        db_table = 'notes'
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


