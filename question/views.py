from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView
#from django.views.generic.edit import UpdateView, DeleteView

from question.models import Question, Comment
from question.forms import QuestionForm, CommentForm


class QuestionListView(ListView):
    """ Renders a list of all Question. """
    model = Question

    def get(self, request):
        """ GET a list of Questions. """
        questions = self.get_queryset().all()
        return render(request, 'index.html', {
          'questions': questions
        })

class QuestionDetailView(DetailView):
    """ Renders a specific question based on it's slug."""
    model = Question

    def get(self, request, slug):
        """ Returns a specific question by slug. """
        question = self.get_queryset().get(slug__iexact=slug)
        comment_form = CommentForm()
        return render(request, 'question.html', {
          'question': question,
          'comment_form': comment_form
        })

    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
          one_comment = form.save(commit=False)
          one_comment.question_id = Question.objects.get(slug__iexact=slug)
          one_comment.save()
          return redirect('question-details-page', slug=slug)

class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
  
class QuestionCreateView(CreateView):
  template = 'new_question.html'
  form_class = QuestionForm
  success_url = '/' 

  def get(self, request):
    form = QuestionForm()
    return render(request, 'new_question.html', {'form': form})
  
  def post(self, request):
    if request.method == 'POST':
      form = QuestionForm(request.POST)
      if form.is_valid():
        log = form.save()
        return HttpResponseRedirect(reverse_lazy('question-details-page', args=[log.slug]))
      return render(request, 'new_question.html', {'form': form})
"""
class QuestionUpdateView(UpdateView):
      def update(request, slug):
        question = Question.objects.get(slug__iexact=slug)
        form = QuestionForm(request.POST or None, instance=question)

        if form.is_valid():
          form.save()
          return redirect('question-details-page', slug=slug)

class QuestionDeleteView(DeleteView):
      def delete(request, slug):
        question = Question.objects.get(slug__iexact=slug)

        if request.method == 'POST':
          question.delete()
          return redirect('index.html')
"""