from datetime import datetime
from dateutil.relativedelta import relativedelta
from northbridge.models import Page, Visits


def user_visit_data(user_id):
    """
    Returns the user visit volume over different time periods
    """

    page_visits = {}
    datetime_mapping = {
        "1 Day": (datetime.now() - relativedelta(days=1)),
        "7 Days": (datetime.now() - relativedelta(days=7)),
        "30 Days": (datetime.now() - relativedelta(days=30)),
        "4 Months": (datetime.now() - relativedelta(months=4)),
        "6 Months": (datetime.now() - relativedelta(months=6)),
        "12 Months": (datetime.now() - relativedelta(months=12))
    }

    for page in Page.objects.all():
        duration_visits = []
        visits = 0
        for label, delta in datetime_mapping.items():
            visits = Visits.objects.filter(
                policy__user_id=user_id, page=page, created__gte=delta.date()).count()
            duration_visits.append(visits)
        page_visits[page.name] = duration_visits

    return page_visits
