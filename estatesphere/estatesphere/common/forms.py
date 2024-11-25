from django import forms
from estatesphere.common.models import Review


class SearchForm(forms.Form):
    property_location = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search properties...'}
        )
    )
    
    
class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'rating', )


class ReviewCreateForm(ReviewBaseForm):
    pass





            
