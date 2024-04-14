from rest_framework import serializers
from .models import Post, User

 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        partial = True  # Enable partial updates


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Make sure password field is write-only
        }
        partial = True  # Enable partial updates