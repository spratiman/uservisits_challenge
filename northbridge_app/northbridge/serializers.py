from rest_framework import serializers
from northbridge.models import User, Policy, Page, Visits


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


class VisitsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Visits model
    """
    created = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    policy = serializers.SlugRelatedField(
        slug_field="hash_id", queryset=Policy.objects.all(), required=True
    )
    page = serializers.SlugRelatedField(
        slug_field="name", queryset=Page.objects.all(), required=True
    )

    class Meta:
        model = Visits
        fields = ("created", "policy", "page")
        read_only_fields = ("created", "policy", "page")
