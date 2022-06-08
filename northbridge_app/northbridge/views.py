from rest_framework_json_api.views import ModelViewSet
from northbridge.serializers import UserSerializer
from northbridge.models import User


class UserAPIView(ModelViewSet):
    serializer_class = UserSerializer
    http_methods = ["get"]
    queryset = User.objects.all()
