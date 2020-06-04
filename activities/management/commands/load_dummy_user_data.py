import sys
import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User


from ...models import User, ActivityPeriod

from django.core.management.base import BaseCommand

from activities.data_factory import ActivityFactory, UserFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=15,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            ActivityFactory.create()

# class Command(BaseCommand):
#     args = 'username...'
#
#     def handle(self, *args, **options):
#         if len(args) == 0:
#             sys.stdout.write('You must specify a username.\n')
#             sys.exit(1)
#
#         try:
#             user = User.objects.get(real_name=args[0])
#         except ObjectDoesNotExist:
#             user = User.objects.create(real_name=args[0])
#             user.id = 'ABC'+random(1000)+'XYZ'
#             user.tz = 'America/Los_Angeles'
#             user.activityperiod_set.create(start_time='2020-01-01 19:30+05:30', end_time='2020-02-01 20:30+05:30')
#             user.save()
#
#             # Create an entry for the User Settings.
#             User.objects.create(user=user).save()
#
#         # Delete existing data.
#         User.objects.filter(user=user).delete()
