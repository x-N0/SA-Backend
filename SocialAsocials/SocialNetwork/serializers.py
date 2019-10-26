from rest_framework import serializers
from .models import User, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'created', 'username', 'first_name', 'last_name', 'email', 'password', 'telephone', 'birth',
            'about_me', 'current_status',
            'amount_friends')
