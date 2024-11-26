from django import forms
from django.core.validators import ValidationError


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class MultiImageUploadForm(forms.Form):
    images = MultipleFileField()

    def clean_images(self):
        files = self.files.getlist('images')
        allowed_content_types = ['image/jpeg', 'image/png', 'image/gif']

        if not files:
            raise ValidationError("No files uploaded.")

        for file in files:
            if file.content_type not in allowed_content_types:
                raise ValidationError(f"Unsupported file type: {file.content_type}. Allowed types are JPEG, PNG, and GIF.")

        return files
