from rest_framework import serializers
from northbridge.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """

    class Meta:
        model = User
        fields = ("name", "email", "is_active")
        read_only_fields = ("name", "email", "is_active")
