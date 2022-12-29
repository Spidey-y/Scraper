from rest_framework import serializers
from .models import User
from re import match


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'address', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    @staticmethod
    def validate_password(val: str):
        if len(val) < 8:
            raise serializers.ValidationError(detail="Password too short")
        return val

    @staticmethod
    def validate_phone_number(val: str):
        if not match(r'^(\+213)?[0-9]{10}$', val):
            raise serializers.ValidationError(detail="Invalid phone number")
        return val

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

