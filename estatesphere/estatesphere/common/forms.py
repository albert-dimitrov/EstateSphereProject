from django import forms


class SearchForm(forms.Form):
    property_location = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search properties...'}
        )
    )
