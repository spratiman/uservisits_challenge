from django.conf.urls import include
from django.urls import re_path
from rest_framework.routers import SimpleRouter
from northbridge.views import PageAPIView, PolicyAPIView, UserAPIView, VisitsAPIView

USERS_ROUTER = SimpleRouter()
USERS_ROUTER.register("", UserAPIView, basename="users")

POLICY_ROUTER = SimpleRouter()
POLICY_ROUTER.register("", PolicyAPIView, basename="policies")

PAGE_ROUTER = SimpleRouter()
PAGE_ROUTER.register("", PageAPIView, basename="pages")

VISITS_ROUTER = SimpleRouter()
VISITS_ROUTER.register("", VisitsAPIView, basename="visits")


urlpatterns = [
    re_path("users/", include(USERS_ROUTER.urls)),
    re_path("policies/", include(POLICY_ROUTER.urls)),
    re_path("pages/", include(PAGE_ROUTER.urls)),
    re_path("visits/", include(VISITS_ROUTER.urls)),
]
