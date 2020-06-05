from django.db import models


class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

    def data(self):
        user_data = {'id': self.id, 'real_name': self.real_name, 'tz': self.tz}
        return user_data


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start time')
    end_time = models.DateTimeField('End time')

    def data(self):
        activity_data = {'user': self.user, 'start_time': self.start_time, 'end_time': self.end_time}
        return activity_data
