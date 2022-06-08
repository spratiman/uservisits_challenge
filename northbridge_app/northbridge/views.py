from rest_framework_json_api.views import ModelViewSet
from northbridge.serializers import UserSerializer, PolicySerializer
from northbridge.models import User, Policy


class UserAPIView(ModelViewSet):
    serializer_class = UserSerializer
    http_methods = ["get"]
    queryset = User.objects.all()


class PolicyAPIView(ModelViewSet):
    serializer_class = PolicySerializer
    http_methods = ["get"]
    queryset = Policy.objects.all()
