import graphene

import graphql_social_auth

from . import mixins
from .testcases import RelaySchemaTestCase


class SocialAuthTests(mixins.SocialAuthMixin, RelaySchemaTestCase):
    query = '''
    mutation SocialAuth($input: SocialAuthInput!) {
      socialAuth(input: $input) {
        result {
          __typename
          ... on Social {
            social {
              uid
              extraData
            }
          }
        }
        clientMutationId
      }
    }'''

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.relay.SocialAuth.Field()


class SocialAuthJWTTests(mixins.SocialAuthJWTMixin,
                         RelaySchemaTestCase):

    query = '''
    mutation SocialAuth($input: SocialAuthJWTInput!) {
      socialAuth(input: $input) {
        result {
          __typename
          ... on JWT {
            social {
              uid
              extraData
            }
            token
          }
        }
        clientMutationId
      }
    }'''

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.relay.SocialAuthJWT.Field()
