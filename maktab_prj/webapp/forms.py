from django import forms
from ajax_select.fields import AutoCompleteSelectField

class LocationForm(forms.Form):
    country = AutoCompleteSelectField('country', required=False, help_text=None)
    state = AutoCompleteSelectField('state', required=False, help_text=None)
    city = AutoCompleteSelectField('city', required=False, help_text=None)

