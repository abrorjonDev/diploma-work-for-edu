from rest_framework import serializers

from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name', 'last_name', 
            'email',
            'password',
            )
    
    def create(self, validated_data):
        user = super().create(validated_data)

        if validated_data.get('password'):
            user.set_password(validated_data.get('password'))
            user.save()
        
        return user