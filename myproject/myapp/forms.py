from django.forms import ModelForm
from . import models
class myform(ModelForm):
    class Meta:
        model=models.details
        fields='__all__'