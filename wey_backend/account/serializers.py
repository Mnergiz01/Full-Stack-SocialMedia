from .models import FriendshipRequest, User 
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email',)

class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    class Meta:
        model = FriendshipRequest
        fields = ('id','created_by',)
