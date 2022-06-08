from django.urls import path
from northbridge.views import display_users, ReportView

urlpatterns = [
    path('', display_users, name='homepage'),
    path(r"users/<int:user_id>/report/",
         ReportView.as_view(), name="user-report")
]
