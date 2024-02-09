from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Circuit
from descriptions.models import Description
from .forms import CircuitForm
from django.views.generic import (
    ListView, 
    FormView,
    DetailView,
    UpdateView,
    CreateView
)
from .forms import CircuitForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
# para trabajar con letras del abecedario
import string

# Create your views here.

class CircuitsListView(FormView, ListView):
    model = Circuit
    # por omisión: circuit_list.html
    # por omisión: object_list
    # para evitar lo anterior, cambiaremos los nombres:
    template_name = 'circuits/main.html'
    queryset = Circuit.objects.all().order_by('circuit_id')
    qs = queryset
    context_object_name = 'qs'
    form_class = CircuitForm

    i_instance = None

    #success_url = reverse_lazy('circuits:main')
    
    # overridinig success_url method
    def get_success_url(self):
        return self.request.path

    #def get_queryset(self):
    #    parameter = 's'
    #    return Program.objects.filter(title_startswith=parameter=) 

    #def get_context_data(self):
    #    context = { 
    #        'form': self.get_form_class(), 
    #        'qs': self.get_queryset(),
    #        'hi': 'hello',
    #        'hi2': 'maryita'
    #    }
    #    return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # abajo otros parametros a pasar al html:
        # context['hi'] = 'un parametro '
        # context['hi2'] = 'otro parametro'
        # las siguientes 2 lineas no sirven en este programa
        #letters = list(string.ascii_uppercase)
        #context['letters'] = letters
    
        return context

    # esto garantiza que se guarde el formulario en la base de datos
    def form_valid(self, form):
        self.i_instance = form.save()
        messages.add_message(self.request, messages.INFO, f"Circuit: {self.i_instance.circuit_id} has been created" )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        self.object_list = self.get_queryset() # a veces se pierde el object_list, hay que reasignarlo
        messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class CircuitDescriptionsListView(ListView):
    model = Circuit
    template_name = 'circuits/circuit_descriptions_list.html'
    #paginate_by = 5
    #context_list llevara los objetos
    #form_class = CircuitForm

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        #obj = Circuit.objects.get(pk=pk)  # es la referencia del objeto padre
        #descriptions = obj.descriptions  # por una property se trata como que fuera un campo
        return Circuit.objects.get(pk=pk).descriptions


#def circuit_descriptions_list_view(request, **kwargs):
#    pk = kwargs.get('pk')
#    obj = Circuit.objects.get(pk=pk)  # es la referencia del objeto padre
#    descriptions = obj.descriptions  # por una property se trata como que fuera un campo
#
#    context = {
#        'obj': obj,
#        'descriptions': descriptions,
#    }
#    return render(request, 'circuits/circuit_descriptions_list.html', context)

class CircuitUpdateView(UpdateView):
    model = Circuit
    template_name = 'circuits/circuit_update.html'
    fields = '__all__'
    #form_class = CircuitForm

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        #obj = Circuit.objects.get(pk=pk_) # alternativa de comando al siguiente
        obj = get_object_or_404(Circuit, pk=pk_)
        print(obj.pk)
        return obj
    
