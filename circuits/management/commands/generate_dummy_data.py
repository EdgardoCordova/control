from django.core.management.base import BaseCommand
from circuits.models import Circuit
from descriptions.models import Description

# para la creacion inicial pueda que este comando de un error
Circuit.objects.all().delete()

class Command(BaseCommand):
    # solamente vamos a generar data para Circuits 
    
    def handle(self, *args, **kwargs):
    # generating Circuits
        circuits_list = [
            {'circuit_id':1001, 'circuit_description': 'Lamparas Camping', 'circuit_status': True,'num_cycles': 5,'num_events': 1,'event_random': False,'event_duration': 60},
            {'circuit_id':1002, 'circuit_description': 'Ventiladores Casa', 'circuit_status': True,'num_cycles': 4,'num_events': 3,'event_random': False,'event_duration': 10},
            {'circuit_id':1003, 'circuit_description': 'Luces Emergencia', 'circuit_status': True,'num_cycles': 6,'num_events': 3,'event_random': True,'event_duration': 2},
            {'circuit_id':1004, 'circuit_description': 'Calentadores Casa', 'circuit_status': True,'num_cycles': 3,'num_events': 1,'event_random': False,'event_duration': 60}
        ]
        for item in circuits_list:
            Circuit.objects.create(**item)

