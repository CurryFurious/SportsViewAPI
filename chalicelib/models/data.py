from marshmallow import Schema, fields
from datetime import datetime
import arrow

class DataModel(Schema):
    x_pos = fields.Decimal()
    y_pos = fields.Decimal()
    hue = fields.Decimal()
    time = fields.String()
