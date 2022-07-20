from django.db.models import JSONField
from django.db import models


class GenericModel(models.Model):
    data = JSONField()

    def __str__(self):
        return self.data

