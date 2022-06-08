from rest_framework import serializers
from northbridge.models import User, Policy, Page


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """

    class Meta:
        model = User
        fields = ("name", "email", "is_active")
        read_only_fields = ("name", "email", "is_active")


class PolicySerializer(serializers.ModelSerializer):
    """
    Serializer for the Policy model
    """

    user = serializers.SlugRelatedField(
        slug_field="email", queryset=User.objects.all(), required=True
    )
    state = serializers.CharField(source='get_state_display')
    start_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")

    class Meta:
        model = Policy
        fields = ("user", "hash_id", "start_date", "state")
        read_only_fields = ("user", "hash_id", "start_date", "state")


class PageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Page model
    """

    class Meta:
        model = Page
        fields = ("name",)
        read_only_fields = ("name",)
