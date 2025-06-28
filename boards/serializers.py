from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Board


USER = get_user_model()

class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    class Meta:
        model = Board
        fields = ['board_name', 'owner', 'tasks_count', 'visibility', 'date_created', 'date_updated']
        

class CreateBoardSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default =  serializers.CurrentUserDefault()) #sets the current user as the owner
    class Meta:
        model = Board
        fields = ['board_name', 'owner', 'visibility']
     