from django import forms
from . import models



class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Questions
        fields = ('text',)


class AnswerForm(forms.ModelForm):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['question'].widget = forms.HiddenInput()


    class Meta:
        model = models.Answers
        fields = ('text', 'question')