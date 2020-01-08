from django.urls import path
from question.views import QuestionListView, QuestionCreateView, QuestionDetailView #QuestionUpdatelView, QuestionDeleteView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list-view'),
    path('new_question/', QuestionCreateView.as_view(), name='question-new-page'),
    path('<str:slug>/', QuestionDetailView.as_view(), name='question-details-page')
]

"""Url links to get the pages to be able to link together. 
A pathway to get from the homepage to create a new question to view an existing question."""
