from django.conf import settings
from django import forms

field_types = {
    str: forms.CharField,
    int: forms.IntegerField,
    float: forms.FloatField,
    bool: forms.BooleanField
}


class SchemaValidator:
    def validate_schema(self, schema: dict) -> None:
        for field_name, field_data in schema.items():
            try:
                field_types.get(field_data["field_type"])(**field_data.get("properties", {}))
            except TypeError as exc:
                raise RuntimeError(f"Invalid property for field '{field_name}' - {exc}")


MODEL_DATA_SCHEMA = getattr(settings, 'GENERIC_MODEL_SCHEMA', None)

if not MODEL_DATA_SCHEMA:
    raise RuntimeError("Generic model schema is not defined.")

if not isinstance(MODEL_DATA_SCHEMA, dict):
    raise RuntimeError("Invalid type for GENERIC_MODEL_SCHEMA, expected type is dict.")

schema_validator = SchemaValidator()
schema_validator.validate_schema(MODEL_DATA_SCHEMA)
