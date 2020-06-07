import datetime
import string

import factory.django
from faker import Faker

from .models import User, ActivityPeriod

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    real_name = factory.Faker('name')
    id = factory.Sequence(lambda n: ''.join(
        fake.random_elements(elements=(string.ascii_uppercase + string.digits), length=9, unique=True)).upper())
    tz = factory.Faker('timezone')


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod

    user = factory.SubFactory(UserFactory)
    start_time = fake.date_time_this_year(before_now=True, after_now=False)
    end_time = fake.date_time_between(start_date=start_time, end_date=start_time + datetime.timedelta(days=1))
