from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=20, unique=True)

    def get_responses(self, quiz):
        return Responses.objects.filter(respondant=self, choice__question__quiz=quiz)

    def get_marks(self, quiz):
        responses = self.get_responses(quiz)
        count = 0
        for item in responses:
            print(item__choice, item__choice.choice_text)
            if item__choice__isAnswer:
                count += item__choice__question__max_marks
        return count


class Quiz(models.Model):
    def __str__(self):
        return self.description_text

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    end_date = models.DateTimeField(
        'end date', default=timezone.now() + datetime.timedelta(days=1))

    def was_published_recently(self):
        return self.pub_date >= timezone.now()
    # datetime.timedelta(days=1)


class Question(models.Model):
    def __str__(self):
        return self.question_text

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    max_marks = models.IntegerField(default=1)


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    isAnswer = models.BooleanField(default=False)


class Responses(models.Model):
    respondant = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
