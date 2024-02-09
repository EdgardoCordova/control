from django.contrib import admin
from .models import Circuit

# import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

class CircuitResource(resources.ModelResource):
    created = Field()
    circuit_status = Field()
    event_random = Field()

    class Meta:
        model = Circuit
        fields = ('circuit_id', 'created', 'circuit_description', 'circuit_status', 'num_cycles', 'num_events','event_duration','event_random')
        export_order = ('created', 'circuit_id', 'circuit_description', 'circuit_status', 'num_cycles', 'num_events','event_duration','event_random')

    def dehydrate_created(self, obj):   # 'created' es el nombre del campo arriba,siempre lleva self,obj
        return obj.created.strftime("%d/%m/%y")  # formato que le damos a la fecha

    def dehydrate_circuit_status(self, obj):   # 'circuit_status' es el nombre del campo arriba,siempre lleva self,obj
        if obj.circuit_status == True:
            resultado = "SI"
        else:
            resultado = "NO"
        return resultado
    
    def dehydrate_event_random(self, obj):   # 'event_random' es el nombre del campo arriba,siempre lleva self,obj
        if obj.event_random == True:
            resultado = "SI"
        else:
            resultado = "NO"
        return resultado
    
class CircuitAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = CircuitResource
    #list_display = ['__str__', 'name', 'country', 'created']
    #list_filter = ['country']
    #search_fields = ['name']

admin.site.register(Circuit, CircuitAdmin)
