from rest_framework import serializers
from .models import CustomUser


class UserCreationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'password', 'confirm_password']
        extra_kwargs ={
            'password':{'style': {'input_type': 'password'},
                        'write_only': True}
        }
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # remove before saving
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True, style = {"input_type": "password"})

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',  'email', 'first_name', 'last_name']
        read_only_fields = ['id', 'email']