from functools import partial
from .settings import MODEL_DATA_SCHEMA, field_types


def get_fields(initials=None):
    fields = {}
    for field_name, field_data in MODEL_DATA_SCHEMA.items():
        initial_value = None
        if initials:
            initial_value = initials.get(field_name, None)
        fields[field_name] = partial(
            field_types[field_data["field_type"]], **field_data.get("properties", {})
        )(initial=initial_value)
    return fields
