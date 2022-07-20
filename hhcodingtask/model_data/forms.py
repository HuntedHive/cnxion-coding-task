import json

from django import forms
from .models import GenericModel
from .utils import get_fields


class GenericModelForm(forms.ModelForm):
    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, instance=instance, **kwargs)
        initials = {}
        if instance:
            initials = json.loads(instance.data)
        self._default_fields = get_fields(initials)
        self.fields.update(self._default_fields)

    def save(self, commit=True):
        self.instance.data = json.dumps(
            {
                field_name: self.cleaned_data[field_name]
                for field_name in self._default_fields.keys()
            }
        )
        return super().save(commit)

    class Meta:
        model = GenericModel
        fields = []
