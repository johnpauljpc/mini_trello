from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers

from .serializers import TaskSerializer
from .models import Task

# Create your views here.
class ListCreateTaskView(ListCreateAPIView):
    """
    API endpoint that allows list of tasks to be viewed, and created.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Require authentication and board ownership

    def get_queryset(self):
        """
        Ensure users only see tasks on boards they own.
        """
        return Task.objects.filter(board__owner=self.request.user)

    def perform_create(self, serializer):
        """
        When creating a task, ensure the specified board belongs to the current user.
        This is also handled by IsBoardOwner permission, but added here for redundancy.
        """
        board = serializer.validated_data.get('board')
        if board and board.owner != self.request.user:
            raise serializers.ValidationError({"board": "You do not have permission to add tasks to this board."})
        serializer.save()


class RetrieveTaskView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a task to be retrieved, updated or deleted.
    Tasks are linked to boards, and a user can only manage tasks on boards they own.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Require authentication and board ownership

    
    def perform_update(self, serializer):
        """
        When updating a task, ensure the specified board (if changed) belongs to the current user.
        """
        board = serializer.validated_data.get('board', serializer.instance.board)
        if board and board.owner != self.request.user:
            raise serializers.ValidationError({"board": "You do not have permission to move tasks to this board."})
        serializer.save()
