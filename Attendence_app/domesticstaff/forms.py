from django import forms
class attendencemark(forms.Form):
    reg_no=forms.IntegerField(label="Regestration number")
    ismarked=forms.BooleanField(label="present or abscent",initial=False,required=False)