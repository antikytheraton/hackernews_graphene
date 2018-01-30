import graphene

from apps.links import schema as links_schema
from apps.users import schema as user_schema


class Query(user_schema.Query, links_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, links_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
