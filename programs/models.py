from django.db import models
from django.urls import reverse
from descriptions.models import Description
from datetime import timedelta, timezone


class Program(models.Model):
    """
    Program class
    """
    circuit_slug = models.OneToOneField(Description, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField(blank=True, editable = True)
    event_date_end = models.DateTimeField(blank=True)
    event_duration = models.SmallIntegerField(default=5)


    def __str__(self):
        return f"{self.circuit_slug}, duration: {self.event_duration} " 

    def save(self, *args, **kwargs):     
        if not self.event_date_end:
            self.event_date_end = self.event_date + timedelta(minutes=self.event_duration)
        super().save(*args, **kwargs)
            