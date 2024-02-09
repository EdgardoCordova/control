from django.db import models
from django.urls import reverse

class Circuit(models.Model):
    """
    Circuit class
    """
    circuit_id = models.SmallIntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    circuit_description = models.CharField(max_length=100)
    circuit_status = models.BooleanField(default=True)
    num_cycles = models.SmallIntegerField(editable=True, default=1)
    num_events = models.SmallIntegerField(editable=True, default=1)
    event_duration = models.SmallIntegerField(default=5)
    event_date = models.DateTimeField(null=True, editable=True)
    event_random = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.circuit_id}" 
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse("circuits:circuit-descriptions-list", kwargs={"pk": self.pk})
    
    # reverse relationship
    # esta propiedad permitira manejar descriptions como un campo de la clase anterior
    @property
    def descriptions(self):
        return self.description_set.all()  # description en singular, _set.all() tiene que ir por reverse relationship
    



