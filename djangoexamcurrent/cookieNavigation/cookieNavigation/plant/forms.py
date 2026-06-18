from django import forms
class potform(forms.Form):
    choice=[('red','red'),('yellow','yellow')]
    pot=forms.ChoiceField(choices=choice,label='select the pot')