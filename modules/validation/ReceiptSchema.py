from marshmallow import Schema, fields, validate
from modules.validation.ReceiptItemSchema import ReceiptItemSchema

class ReceiptSchema(Schema):
    retailer = fields.Str(required=True, validate=validate.Regexp(r'^[\w\s\-&]+$', error="Invalid retailer format."))
    purchaseDate = fields.Date(required=True)
    purchaseTime = fields.Time(format='%H:%M', required=True)
    items = fields.List(fields.Nested(ReceiptItemSchema()), required=True, validate=validate.Length(min=1, error="Items list must contain at least one item."))
    total = fields.Str(required=True, validate=validate.Regexp(r'^\d+\.\d{2}$', error="Invalid total format."))