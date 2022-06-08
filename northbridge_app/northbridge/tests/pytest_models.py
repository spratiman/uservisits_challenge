import pytest

from northbridge.models import User, Page, Policy, Visits


@pytest.mark.django_db
def test_retrieve_user_model(user_visit_setup):
    assert len(User.objects.all()) == 3


@pytest.mark.django_db
def test_retrieve_page_model(user_visit_setup):
    assert len(Page.objects.all()) == 3


@pytest.mark.django_db
def test_retrieve_policy_model(user_visit_setup):
    assert len(Policy.objects.all()) == 3


@pytest.mark.django_db
def test_retrieve_visits_model(user_visit_setup):
    assert len(Visits.objects.all()) == 6
