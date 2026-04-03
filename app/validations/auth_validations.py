from marshmallow import Schema, fields, validates, ValidationError


class RegisterSchema(Schema):
    username = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )
    password = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )
    first_name = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )
    last_name = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )
    middle_name = fields.Str(load_default=None)
    birth_date = fields.Date(load_default=None)
    gender = fields.Str(load_default=None)

    @validates("username")
    def validate_username(self, value, **kwargs):
        if not value.strip():
            raise ValidationError("must not be blank")
        if len(value) > 255:
            raise ValidationError("must not exceed 255 characters")

    @validates("password")
    def validate_password(self, value, **kwargs):
        if len(value) < 8:
            raise ValidationError("must be at least 8 characters")

    @validates("first_name")
    def validate_first_name(self, value, **kwargs):
        if not value.strip():
            raise ValidationError("must not be blank")

    @validates("last_name")
    def validate_last_name(self, value, **kwargs):
        if not value.strip():
            raise ValidationError("must not be blank")

    @validates("gender")
    def validate_gender(self, value, **kwargs):
        if value is None:
            return
        allowed = {"male", "female", "other"}
        if value.lower() not in allowed:
            raise ValidationError(f"must be one of: {', '.join(sorted(allowed))}")


class LoginSchema(Schema):
    username = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )
    password = fields.Str(
        required=True,
        error_messages={"required": "is required"}
    )
