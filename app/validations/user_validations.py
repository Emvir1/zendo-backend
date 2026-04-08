from marshmallow import Schema, fields, validates, ValidationError, pre_load


class UserSchema(Schema):
    username = fields.Str(load_default=None)
    first_name = fields.Str(load_default=None)
    last_name = fields.Str(load_default=None)
    middle_name = fields.Str(load_default=None)
    birth_date = fields.Date(load_default=None)
    gender = fields.Str(load_default=None)

    @pre_load
    def normalize_birth_date(self, data, **kwargs):
        if data.get("birth_date"):
            try:
                y, m, d = data["birth_date"].split("-")
                data["birth_date"] = f"{y}-{int(m):02d}-{int(d):02d}"
            except (ValueError, AttributeError):
                pass
        return data

    @validates("username")
    def validate_username(self, value, **kwargs):
        if value is None:
            return
        if not value.strip():
            raise ValidationError("must not be blank")
        if len(value) > 255:
            raise ValidationError("must not exceed 255 characters")

    @validates("first_name")
    def validate_first_name(self, value, **kwargs):
        if value is None:
            return
        if not value.strip():
            raise ValidationError("must not be blank")

    @validates("last_name")
    def validate_last_name(self, value, **kwargs):
        if value is None:
            return
        if not value.strip():
            raise ValidationError("must not be blank")

    @validates("gender")
    def validate_gender(self, value, **kwargs):
        if value is None:
            return
        allowed = {"male", "female", "other"}
        if value.lower() not in allowed:
            raise ValidationError(f"must be one of: {', '.join(sorted(allowed))}")
