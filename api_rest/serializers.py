from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['chave_id', 'user_nickname', 'user_name', 'user_email', 'user_age'] # ou '__all__'