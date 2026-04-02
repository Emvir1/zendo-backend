from marshmallow import Schema, fields, validates, ValidationError

class TaskSchema(Schema):
    title = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )
    description = fields.Str(load_default=None)
    status = fields.Str(load_default="pending")

    @validates("title")
    def validate_title(self, value, **kwargs):
        if not value.strip():
            raise ValidationError("must not be blank")
        if len(value) > 255:
            raise ValidationError("must not exceed 255 characters")

