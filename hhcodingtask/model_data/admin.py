from django.contrib import admin

from .forms import GenericModelForm
from .utils import get_fields
from .models import GenericModel


class GenericModelAdmin(admin.ModelAdmin):
    form = GenericModelForm

    def get_fields(self, request, obj=None):
        gf = super().get_fields(request, obj)
        self.form.declared_fields.update(get_fields())
        return gf


admin.site.register(GenericModel, GenericModelAdmin)
