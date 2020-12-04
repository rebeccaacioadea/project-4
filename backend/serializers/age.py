from app import ma
from serializers.base import BaseSchema
# from serializers.book import BookSchema
from marshmallow import fields
from models.age import Age

class AgeSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Age
    load_instance = True

  # books = fields.Nested('BookSchema', many=True)

