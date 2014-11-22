__author__ = 'Himanshu'

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import StrictButton, FieldWithButtons
from .models import Hospital
from django import forms

class HospitalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HospitalForm, self).__init__(*args, **kwargs)

        # Assign attributes to each field
        for key in self.fields:
            # Assign classes (for CSS decoration and JavaScript validation)
            self.fields[key].widget.attrs['class'] = 'form-control'
            # Assign the autocomplete feature
            self.fields[key].widget.attrs['autocomplete'] = 'on'
            self.fields[key].widget.attrs['name'] = ''
        # Assign form field placeholders
        # Assign JavaScript validation messages
        self.fields['subsidy'].widget.attrs.update({'placeholder': 'Subsidized / Free Treatments Available',})


    class Meta:
        model = Hospital
        fields = '__all__'



