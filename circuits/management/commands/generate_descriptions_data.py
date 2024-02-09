from django.core.management.base import BaseCommand
from circuits.models import Circuit
from descriptions.models import Description
from django.utils.text import slugify


class Command(BaseCommand):
    # vamos a generar data para Descriptions
    
    descriptions_list = []
    Description.objects.all().delete()

    def handle(self, *args, **kwargs):
        # generating Descriptions
        qs1 = Circuit.objects.all()
        
        # loop lectura circuitos
        for item1 in qs1:
            print(item1.id)
            if item1.circuit_status is True:   # si el estatus es False no genera el circuito

                # loop por cada circuito, se corren num de clycles
                for i in range(item1.num_cycles):
                    i = i + 1
                    # loop por cada circuito, se corren num de events
                    for j in range(item1.num_events):
                        j = j + 1
                        
                        cycle = i
                        event = j
                        event_duration = item1.event_duration
                        #item1.event_random 
                        data = Description(circuit_id_id=item1.circuit_id,cycle=i, event=j, event_duration=item1.event_duration)
                        #print(data)

                        exist = Description.objects.filter(circuit_id=item1.circuit_id,cycle=cycle,event=event).exists()
                        print(exist)
                        if not exist:
                            circuit_slug = slugify(f"{item1.circuit_id} {cycle} {event}")
                            print(circuit_slug)
                            Description.objects.create(circuit_id_id=item1.id,cycle=i, event=j, event_duration=item1.event_duration, circuit_slug=circuit_slug)
                            
                            
        #Description.objects.create(**item1)
        

        





