from django import forms

from estatesphere.contacts.models import Massages


class MassageBaseForm(forms.ModelForm):
    class Meta:
        model = Massages
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type your message...',
            })
        }


class MassageAddForm(MassageBaseForm):
    pass