from django import forms
from apps.example_sites.models import PythonWebBasicsModel


class PythonWebBasicsBaseForm(forms.ModelForm):
    class Meta:
        model = PythonWebBasicsModel
        fields = '__all__'
