from rest_framework import serializers
from .models import customUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return customUser.objects.create_user(**validated_data)