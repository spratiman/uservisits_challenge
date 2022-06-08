from django.urls import path
from northbridge.views import display_users

urlpatterns = [
    path('', display_users, name='homepage'),
]
