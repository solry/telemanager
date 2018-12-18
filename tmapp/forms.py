from django import forms
from .models import Command

class CommandChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    genre = forms.ModelMultipleChoiceField(
        queryset=Command.objects.all(), required=False)