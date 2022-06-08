import pytest

from rest_framework.test import APIClient
from model_bakery import baker
from northbridge.models import User, Page, Policy, Visits


@pytest.fixture
def user_visit_setup():
    # Create test users
    user1 = baker.make(User)
    user2 = baker.make(User)
    user3 = baker.make(User)

    # Create test pages
    page1 = baker.make(Page, name="/home-page")
    page2 = baker.make(Page, name="/thank-you")
    page3 = baker.make(Page, name="/sorry")

    # Create policies for the users
    policy1 = baker.make(Policy, user=user1)
    policy2 = baker.make(Policy, user=user2)
    policy3 = baker.make(Policy, user=user3)

    # Generate page visit logs for the users
    baker.make(Visits, policy=policy1, page=page1)
    baker.make(Visits, policy=policy2, page=page1)
    baker.make(Visits, policy=policy2, page=page2)
    baker.make(Visits, policy=policy3, page=page1)
    baker.make(Visits, policy=policy3, page=page2)
    baker.make(Visits, policy=policy3, page=page3)

    return {"user1": user1, "user2": user2, "user3": user3}


@pytest.fixture
def api_client():
    return APIClient()
