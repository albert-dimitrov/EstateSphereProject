from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from estatesphere.accounts.models import Profile


UserModel = get_user_model()


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'pofile_picture': forms.TextInput(attrs={'type': 'text'})
        }