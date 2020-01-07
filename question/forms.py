from django import forms
from question.models import Question, Comment

class QuestionForm(forms.ModelForm):
    """ Render and process a form based on the Question model. """
    class Meta:
        model = Question
        fields = '__all__'

class CommentForm(forms.ModelForm):
    """ Render and process a form based on the Comment model. """
    class Meta:
        model = Comment
        fields = ['comment']