from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    Read-only fields for board name and owner for context.
    """
    board_name = serializers.ReadOnlyField(source='board.name')
    board_owner_username = serializers.ReadOnlyField(source='board.owner.first_name')

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'board', 'board_name', 'board_owner_username',
                  'status', 'due_date', 'date_created', 'date_updated')
        read_only_fields = ('date_created', 'date_updated')

# class CreateTaskSerializer(serializers.ModelSerializer)