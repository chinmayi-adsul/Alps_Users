import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery


"""
class CustomRegister(mutations.Register):
   refresh_token = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        # Extract the refresh_token argument
         refresh_token = kwargs.pop('refresh_token', None)

        # Your registration logic here
        return super().mutate(root, info, **kwargs)
"""

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
