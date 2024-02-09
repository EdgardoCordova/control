from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.http import HttpResponse
from .models import Description
from .forms import DescriptionForm
from circuits.models import Circuit 
from .models import Description
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView,
    UpdateView,
    CreateView,
)
# Create your views here.
class DescriptionsListView(ListView):
    model = Description
    template_name = 'descriptions/main.html'
    queryset = Description.objects.all()
    qs = queryset
    #print(qs)
    context_object_name = 'qs'


class CircuitDescriptionUpdateView(UpdateView):
    model = Description
    template_name = 'descriptions/circuit_description_update.html'
    fields = '__all__'
    from_class = DescriptionForm

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        #obj = Description.objects.get(pk=pk_) # alternativa de comando al siguiente
        obj = get_object_or_404(Description, pk=pk_)
        return obj

def circuit_descriptions_generation_view(request, **kwargs):
    pk_ = kwargs.get('pk')
    obj = get_object_or_404(Circuit, pk=pk_)
    i_instance = None
    print(obj)
    context = {
        'obj': obj,
    }
    #return render(request, 'descriptions/circuit_descriptions_generation.html')
    print(context)
    print(request)
    return render(request, 'descriptions/circuit_descriptions_generation.html', context)

def circuit_descriptions_run_view(request, **kwargs):
    print("run")
    #if request.method=='POST':

    pk_ = kwargs.get('pk')
    obj = get_object_or_404(Circuit, pk=pk_)
    print("run ")
    # primero se borran todos las descriptions del circuito seleccionado
    Description.objects.filter(circuit_id_id = pk_ ).delete()
    
    # loop por cada circuito, se corren num_cycles
    for i in range(obj.num_cycles):
        i = i + 1
        # loop por cada circuito, se corren num_events
        for j in range(obj.num_events):
            j = j + 1
            
            cycle = i
            event = j
            event_duration = obj.event_duration
            #item1.event_random 
            data = Description(circuit_id_id=obj.circuit_id,cycle=i, event=j, event_duration=obj.event_duration)
            #print(data)

            exist = Description.objects.filter(circuit_id=obj.circuit_id,cycle=cycle,event=event).exists()
            print(exist)
            if not exist:
                circuit_slug = slugify(f"{obj.circuit_id} {cycle} {event}")
                print(circuit_slug)
                Description.objects.create(circuit_id_id=obj.id,cycle=i, event=j, event_duration=obj.event_duration, circuit_slug=circuit_slug)
                
    #messages.add_message(request, messages.INFO, f"Circuit: {circuit_slug} has been generated" )
    
    context = {
        'obj': obj,
    }
    
    return render(request, 'descriptions/circuit_descriptions_run.html', context)
    
