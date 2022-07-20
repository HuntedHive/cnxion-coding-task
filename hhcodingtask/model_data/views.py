from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse

from .forms import GenericModelForm
from .models import GenericModel


class GenericModelFormView(FormView):
    form_class = GenericModelForm
    template_name = "model_data/model_data_form.html"
    model = GenericModel

    def form_valid(self, form):
        """
        Save instance if form valid.
        """
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Model data successfully added.")
        return reverse("model_data")
