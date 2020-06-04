from django.urls import path

from . import views

app_name = 'activities'
urlpatterns = [
    path('', views.index, name='index'),

    # path('user_activity/<str:id>/', views.user_activity, name='user_activity'),
    #
    # path('list', views.activity_period_list, name='activity_period_list')
]