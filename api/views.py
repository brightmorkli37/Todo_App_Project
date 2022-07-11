from django.utils import timezone
from rest_framework import generics, permissions
from .serializers import TodoCompleteSerializer, TodoSerializer
from todo.models import Todo


class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, status=Todo.Status.DONE)
    

class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    # not required since queryset is already filtered by user
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class TodoUpdate(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.status = Todo.Status.DONE
        serializer.instance.datecompleted = timezone.now()
        serializer.save()