import datetime
import random

from django.core.management.base import BaseCommand
from faker import Faker

from activities.data_factory import ActivityFactory, UserFactory

fake = Faker()


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
                            default=1,
                            type=int,
                            help='The number of fake users to create.')

    def handle(self, *args, **options):
        print('executing!..')
        user_list = UserFactory.create_batch(options['users'])
        for user in user_list:
            months = random.randint(1, datetime.date.today().month)
            for _ in range(months):
                start_time = fake.date_time_this_year(before_now=True, after_now=False)
                end_time = fake.date_time_between(start_date=start_time,
                                                  end_date=start_time + datetime.timedelta(days=1))
                ActivityFactory.create(user=user, start_time=start_time, end_time=end_time)
        return
