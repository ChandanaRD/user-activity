from django.shortcuts import render

from .models import User, ActivityPeriod


def index(request):
    response = {"ok": True, "members": []}
    user_list = User.objects.all().order_by('real_name')
    user_activity_list = []
    for user in user_list:
        user_data = user.data()
        user_data['activity_periods'] = []
        activity_periods = ActivityPeriod.objects.filter(user=user).order_by('start_time')
        for activity in activity_periods:
            activity_data = activity.data()
            del activity_data["user"]
            user_data['activity_periods'].append(activity_data.copy())
        user_activity_list.append(user_data)
    response['members'] = user_activity_list
    context = {'user_list': response}
    return render(request, 'activities/index.html', context)


