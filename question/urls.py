from django.urls import path
from question.views import QuestionListView, QuestionCreateView, QuestionDetailView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list-view'),
    path('new_question/', QuestionCreateView.as_view(), name='question-new-page'),
    path('<str:slug>/', QuestionDetailView.as_view(), name='question-details-page')
]
