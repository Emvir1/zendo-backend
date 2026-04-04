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


class TaskUpdateSchema(Schema):
    title = fields.Str(load_default=None)
    description = fields.Str(load_default=None)
    status = fields.Str(load_default=None)

    @validates("title")
    def validate_title(self, value, **kwargs):
        if value is None:
            return
        if not value.strip():
            raise ValidationError("must not be blank")
        if len(value) > 255:
            raise ValidationError("must not exceed 255 characters")

    @validates("status")
    def validate_status(self, value, **kwargs):
        if value is None:
            return
        allowed = {"pending", "completed"}
        if value not in allowed:
            raise ValidationError(f"must be one of: {', '.join(sorted(allowed))}")

