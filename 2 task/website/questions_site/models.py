from django.db import models
from django.urls import reverse


class Questions(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.pk})

    def answers(self):
        return Questions.objects.order_by('id')
    def answers1(self):
        return Answers.objects.filter(question=self.pk)


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.question_id})

    def __str__(self):
        return self.text