import django
import os
import random
from django.db.utils import IntegrityError
from faker import Faker
from random import choice

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "northbridge_app.settings")

django.setup()


def main():
    from northbridge.models import Page, User, Policy, Visits

    fake = Faker()

    # Populate the list of Page
    names = ["/home-page", "/thank-you", "/sorry", "/checkout", "/about-us"]
    for name in names:
        Page.objects.create(name=name)

    # Populate User
    for _ in range(25):
        User.objects.create(
            name=fake.name(),
            email=fake.unique.ascii_free_email(),
            is_active=fake.boolean()
        )

    # Populate Policy
    for _ in range(50):
        random_user = random.choice(User.objects.all())
        try:
            Policy.objects.create(
                user=random_user,
                start_date=fake.date_time(),
                state=choice(["P", "A", "E"])
            )
        except IntegrityError:
            continue

    # Populate Visits
    for _ in range(100):
        random_page = random.choice(Page.objects.all())
        random_policy = random.choice(Policy.objects.all())
        Visits.objects.create(
            policy=random_policy,
            page=random_page,
            created=fake.date_time_between(
                start_date='-1y')
        )


main()
