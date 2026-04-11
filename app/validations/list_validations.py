from marshmallow import Schema, fields, ValidationError


class ListSchema(Schema):
    name = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )

    @staticmethod
    def validate_name(value, **kwargs):
        if not value.strip():
            raise ValidationError("must not be blank")
        if len(value) > 255:
            raise ValidationError("must not exceed 255 characters")

