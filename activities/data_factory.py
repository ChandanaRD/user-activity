import datetime
import string

import factory
import factory.django
import pytz
from faker import Faker
from faker.providers import BaseProvider
from numpy.random import randint, random, choice
import random as rand

from .models import User, ActivityPeriod
fake = Faker()

class MyProvider(BaseProvider):
    def get_user_id(self):
        prefix = ''.join(rand.choice(string.ascii_letters) for _ in range(3)).upper()
        suffix = ''.join(rand.choice(string.ascii_letters) for _ in range(3)).upper()
        # id = ''.join([prefix, random.choice(range(100, 999)), suffix])
        x = ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        return x;

    def get_timezone(self):
        return choice(pytz.all_timezones)

    def date_time(self):
        start_date = datetime.date(year=2020, month=1, day=1, )
        return fake.date_between(start_date=start_date, end_date='+1y')


fake.add_provider(MyProvider)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    real_name = factory.Faker('name')
    id = fake.get_user_id()
    tz = fake.get_timezone()


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod

    user = factory.SubFactory(UserFactory)
    start_time = fake.date_time()
    end_time = fake.date_time()

