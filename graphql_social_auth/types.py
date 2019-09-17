from graphene.types.generic import GenericScalar
from graphene_django.types import DjangoObjectType
from social_django import models as social_models

from .utils import dashed_to_camel


class CamelJSON(GenericScalar):

    @classmethod
    def serialize(cls, value):
        return dashed_to_camel(value)

    class Meta:
        name = 'SocialCamelJSON'


class Social(DjangoObjectType):
    extra_data = CamelJSON()

    class Meta:
        model = social_models.UserSocialAuth

    def resolve_extra_data(self, info, **kwargs):
        self.extra_data.pop('access_token', None)
        return self.extra_data


class Partial(DjangoObjectType):
    data = CamelJSON()

    class Meta:
        model = social_models.Partial

    def resolve_data(self, info, **kwargs):
        self.data.pop('token', None)
        return self.data
