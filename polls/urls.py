from django.urls import path
from . import apiviews

app_name = 'polls'
urlpatterns = [
    path('login/', apiviews.login, name='login'),
    # poll
    path('poll/create/', apiviews.poll_create, name='poll_create'),
    path('poll/update/<int:poll_id>/', apiviews.poll_update, name='poll_update'),
    path('poll/view/', apiviews.polls_view, name='polls_view'),
    path('poll/view/active/', apiviews.active_polls_view, name='active_poll_view'),
    # question
    path('question/create/', apiviews.question_create, name='question_create'),
    path('question/update/<int:question_id>/', apiviews.question_update, name='question_update'),
    # choice
    path('choice/create/', apiviews.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', apiviews.choice_update, name='choice_update'),
    # answer
    path('answer/create/', apiviews.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', apiviews.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', apiviews.answer_update, name='answer_update')
]