from django import forms
from .models import Circuit
from django.core.exceptions import ValidationError

class CircuitForm(forms.ModelForm):
    class Meta:
        model = Circuit
        fields = '__all__'

    def clean(self):
        circuit_id = self.cleaned_data.get('circuit_id')

        if len(str(circuit_id)) < 4:
            error_msg = 'the circuit id is too short'
            #self.add_error('circuit_id',error_msg)
            raise ValidationError(error_msg)

        elif len(str(circuit_id)) > 4:
            error_msg = 'The circuit id is too long'
            #self.add_error('circuit_id',error_msg)
            raise ValidationError(error_msg)

        num_cycles = self.cleaned_data.get('num_cycles')
        if num_cycles < 1:
            error_msg = 'Number of cycles has to be greater than 1'
            #self.add_error('num_cycles',error_msg)
            raise ValidationError(error_msg)
        
        num_events = self.cleaned_data.get('num_events')
        if num_events < 1:
            error_msg = 'Number of events has to be greater than 1'
            #self.add_error('num_events',error_msg)
            raise ValidationError(error_msg)
        
        circuit_exists = Circuit.objects.filter(circuit_id__iexact=circuit_id).exists()
        if circuit_exists:
            error_msg = 'Circuit already exists'
            raise ValidationError(error_msg)

        return self.cleaned_data

            



