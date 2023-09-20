
from rest_framework import serializers

from api.v1.accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', "email", "username", "password", "last_name", "first_name")
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
        
    def create(self, validated_data):
        user = CustomUser.object.create(username=validated_data['username'],
                                        email=validated_data['email'],
                                        last_name=validated_data['last_name'],
                                        first_name=validated_data['first_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user