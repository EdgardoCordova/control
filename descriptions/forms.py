from django import forms
from .models import Description
from django.core.exceptions import ValidationError

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = '__all__'
    
    #def clean(self):
    #    circuit_slug = self.cleaned_data.get('circuit_id')

        #if len(str(circuit_id)) < 4:
        #    error_msg = 'the circuit id is too short'
        #    #self.add_error('circuit_id',error_msg)
        #    raise ValidationError(error_msg)

        #elif len(str(circuit_id)) > 4:
        #    error_msg = 'The circuit id is too long'
        #    #self.add_error('circuit_id',error_msg)
        #    raise ValidationError(error_msg)

      
        #return self.cleaned_data

            



