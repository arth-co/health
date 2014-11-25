__author__ = 'Himanshu'


from .models import Hospital, City
from django import forms
from django.forms import TypedChoiceField, TypedMultipleChoiceField
from django.forms.widgets import TextInput

class HospitalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HospitalForm, self).__init__(*args, **kwargs)
        self.fields.pop('created_by')
        self.fields.pop('edited_by')

        # Assign attributes to each field
        for key in self.fields:
            # Assign classes (for CSS decoration and JavaScript validation)
            #self.fields[key].widget.attrs['class'] = 'form-control'
            # Assign the autocomplete feature

            self.fields[key].widget.attrs['autocomplete'] = 'off'
            self.fields[key].widget.attrs.update({'placeholder': self.fields[key].label, 'class':'form-control '})
            #self.fields[key].label = ''

               #self.fields[key].empty_label = self.fields[key].label
        # Assign form field placeholders
        # Assign JavaScript validation messages
        #self.fields['subsidy'].widget = forms.text
        #self.fields['subsidy'].widget.attrs.update({'placeholder': 'Subsidized / Free Treatments Available', 'class':'form-control '})



    class Meta:
        model = Hospital
        fields = '__all__'



class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'