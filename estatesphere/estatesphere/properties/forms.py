from django import forms
from estatesphere.properties.models import RealEstateProperty


class PropertyBaseForm(forms.ModelForm):
    class Meta:
        model = RealEstateProperty
        exclude = ('user', 'created_at', 'updated_at',)
        widgets = {
            'price': forms.NumberInput(attrs={'placeholder': 'This is a price in EUR! Example:888888.88'}),
            'area': forms.NumberInput(attrs={'placeholder': 'This is a area in (sq.m)!'})
        }


class PropertyCreateForm(PropertyBaseForm):
    pass


class PropertyEditForm(PropertyCreateForm):
    pass
