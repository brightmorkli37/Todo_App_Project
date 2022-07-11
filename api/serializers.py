from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['id', 'created', 'datecompleted', 'user']


class TodoCompleteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ['id']
        # read_only_fields = ['title', 'memo', 'priority', 'status', 'created', 'datecompleted', 'important', 'user']