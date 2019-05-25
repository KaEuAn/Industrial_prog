from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ask', views.AskView.as_view(), name='ask'),
    path('answer', views.AnswersView.as_view(), name='answer'),
    path('quest_<int:pk>', views.QuestionsView.as_view(), name='question'),
]

    