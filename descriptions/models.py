from django.db import models
from django.urls import reverse
from circuits.models import Circuit
from django.utils.text import slugify

class Description(models.Model):
    """
    Description class
    """
    circuit_id = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cycle = models.SmallIntegerField(default=1)
    event = models.SmallIntegerField(default=1)
    event_date = models.DateTimeField(null=True, editable = True)
    event_duration = models.SmallIntegerField(default=5)
    circuit_slug = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.circuit_id} - {self.cycle} - {self.event} " 

    def get_absolute_url(self):
        circuit_slug = self.circuit_slug
        return reverse("circuits:circuit-descriptions-edit", {"circuit_slug": circuit_slug})
    
    def get_absolute_url_b(self):
        pk = self.pk
        return reverse("descriptions:circuit-description-detail", {"pk": pk})
    

