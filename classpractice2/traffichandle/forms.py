from django import forms

class trafficForm(forms.Form):
    timePeriod = forms.DurationField(label='enter the duration',)