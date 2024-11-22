from marshmallow import Schema, fields, validate

class ReceiptItemSchema(Schema):
    shortDescription = fields.Str(required=True, validate=validate.Regexp(r'^[\w\s\-]+$', error="Invalid item description format."))
    price = fields.Str(required=True, validate=validate.Regexp(r'^\d+\.\d{2}$', error="Invalid item price format."))