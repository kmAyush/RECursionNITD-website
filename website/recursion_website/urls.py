from django.urls import path
from .views import *
from django.conf.urls import include,url
from django.conf import settings

urlpatterns = [
    path('add', add_question, name='add_question'),
    path('', list_questions ,name='list_questions'),
    path('detail/<int:id>/', detail_questions, name='detail_questions'),
    path('update/<int:id>/', update_questions, name='update_question'),
    path('viewprofile/<str:username>/', view_profile, name='view_profile'),
    path('question/<int:id>/answer',add_answer,name='add_answer'),
    path('answer/<int:id>',update_answer,name='update_answer'),
    path('answer/<int:id>/vote', voting, name='voting'),
    path('follow/<int:id>/', edit_following, name='edit_following'),
    path('comment/<int:id>/', add_comment, name='add_comment'),
    path('editcomment/<int:id>/', update_comment, name='update_comment'),
    path('createprofile/<str:username>/', create_profile, name='create_profile'),
    path('register/', user_register, name="user_register"),
    path('updateprofile/<str:username>/', update_profile, name='update_profile'),
    path('filter/<int:id>/', filter_question, name='filter_question'),
    path('events_list/',events, name='events'),
    path('event_detail/<int:id>/', event_detail, name='event_detail'),
    path('event_update/<int:id>/', event_update, name='event_update'),
    path('upcoming_event_list/',upcoming_events, name='upcoming_events'),
]
