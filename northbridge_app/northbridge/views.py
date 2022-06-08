from django.shortcuts import render
from rest_framework_json_api.views import ModelViewSet
from northbridge.serializers import UserSerializer, PolicySerializer, PageSerializer, VisitsSerializer
from northbridge.models import User, Policy, Page, Visits


class UserAPIView(ModelViewSet):
    serializer_class = UserSerializer
    http_methods = ["get"]
    queryset = User.objects.all()


class PolicyAPIView(ModelViewSet):
    serializer_class = PolicySerializer
    http_methods = ["get"]
    queryset = Policy.objects.all()


class PageAPIView(ModelViewSet):
    serializer_class = PageSerializer
    http_methods = ["get"]
    queryset = Page.objects.all()


class VisitsAPIView(ModelViewSet):
    serializer_class = VisitsSerializer
    http_methods = ["get"]
    queryset = Visits.objects.all()


def display_users(request):
    """
    Fetch all users and render the data in a table view
    """

    users = User.objects.all()
    context = {"users": users}
    return render(request, "index.html", context)
