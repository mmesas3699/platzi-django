from django import forms
from countries.models import Country


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='first name')
    nacionality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
