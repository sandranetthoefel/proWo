from django.conf import settings
from django.db import models
from django.utils import timezone


class Projekt(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    klasse = models.IntegerField()
    teilnehmer = models.IntegerField()
    zielgruppe = models.TextField()
    sonstiges = models.TextField()
    docs = models.FileField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
