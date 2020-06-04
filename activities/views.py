from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import User,ActivityPeriod


def index(request):
    user_list = User.objects.order_by('real_name')
    print(user_list);

    context = {'user_list': user_list}
    return render(request, 'activities/index.html', context)

#
# def activity_period_list(request):
#     return HttpResponse("You're looking at question %s.")
#
#
# def user_activity(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     return render(request, 'polls/user_activity.html', {'user': user})

