from marshmallow import Schema, fields

class PositionModel(Schema):
    x = fields.Decimal()
    y = fields.Decimal()
    time = fields.String()


class PlayerModel(Schema):
    playerId = fields.Integer()
    position = fields.Nested(PositionModel, many=True)
    speed = fields.List(fields.Decimal())
    distanceTraveled = fields.List(fields.Decimal())
    timeDiff = fields.List(fields.Decimal())
    averageHue = fields.Decimal()


class CondensedModel(Schema):
    playerId = fields.Integer()
    speed = fields.Decimal()
    distance = fields.Decimal()
    time = fields.Decimal()
    averageHue = fields.Decimal()
