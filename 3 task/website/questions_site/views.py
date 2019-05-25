from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect
from .models import Questions, Answers
from .forms import QuestionForm, AnswerForm


class IndexView(ListView):

    model = Questions
    template_name = 'index.html'

    def get_queryset(self):
        return Questions.objects.order_by('-id')


class QuestionsView(DetailView):

    model = Questions
    template_name = 'question.html'

    def get_form(self):
        return AnswerForm(initial={'question': self.kwargs['pk']})


class AnswersView(CreateView):

    model = Answers
    form_class = AnswerForm

    def get(self, request):
        return redirect('/')


class AskView(CreateView):

    model = Questions
    form_class = QuestionForm
    template_name = 'ask.html'