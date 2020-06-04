from django.db import models


class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start time')
    end_time = models.DateTimeField('End time')

    def __str__(self):
        return self.start_time.__str__()