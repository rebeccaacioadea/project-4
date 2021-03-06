from app import ma
from serializers.base import BaseSchema
from marshmallow import fields
from models.comment import Comment
from models.user import User


class CommentSchema(ma.SQLAlchemyAutoSchema, BaseSchema):

  class Meta:
    model = Comment
    load_instance = True

    load_only = ('user_id',)

  user_id = fields.Integer()

  user = fields.Nested('UserSchema', only=('id', 'username'))
