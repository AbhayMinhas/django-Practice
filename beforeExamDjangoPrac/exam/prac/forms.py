from django import forms
class userform(forms.Form):
    name=forms.CharField(label="enter your name",max_length=100)
    gender=forms.ChoiceField(choices=[('Male','male'),('Female','Female')],label='select your gender')
