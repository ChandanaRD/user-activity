from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import User,ActivityPeriod


def index(request):
    response = {"ok": True, "members": []}
    user_list = User.objects.all()
    user_activity_list = []
    for user in user_list:
        user_data = user.data()
        user_data['activity_periods'] = []
        activity_periods = ActivityPeriod.objects.filter(user=user)
        for activity in activity_periods:
            activity_data = activity.data()
            del activity_data["user"]
            user_data['activity_periods'].append(activity_data.copy())
        user_activity_list.append(user_data)
    response['members'] = user_activity_list
    context = {'user_list': response}
    return render(request, 'activities/index.html', context)

#
# def activity_period_list(request):
#     return HttpResponse("You're looking at question %s.")
#
#
# def user_activity(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     return render(request, 'polls/user_activity.html', {'user': user})

