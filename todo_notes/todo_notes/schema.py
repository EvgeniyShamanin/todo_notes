import graphene

from graphene_django import DjangoObjectType
from user.models import User
from main.models import Todo, Project


class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        id = graphene.ID()

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, text, id):
        todo = Todo.objects.get(pk=id)
        todo.text = text
        todo.save()

        return TodoMutation(todo=todo)


class Query(graphene.ObjectType):

    all_users = graphene.List(UserType)

    all_todo = graphene.List(TodoType)

    all_projects = graphene.List(ProjectType)

    user_by_uuid = graphene.Field(UserType, uuid=graphene.UUID(required=True))

    projects_by_user_username = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    def resolve_all_project(root, info):
        return Project.objects.all()

    def resolve_user_by_uuid(self, info, uuid):
        try:
            return User.objects.get(uuid=uuid)
        except User.DoesNotExist:
            return None

    def resolve_projects_by_user_username(self, info, username=None):
        projects = Project.objects.all()

        if username:
            projects = projects.filter(users__username=username)
            return projects


class Mutation(graphene.ObjectType):
    update_todo = TodoMutation.Field()


schema = graphene.Schema(query=Query)

schema = graphene.Schema(query=Query, mutation=Mutation)