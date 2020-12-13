from django.db import models
from django.utils import timezone
import datetime


class Quiz(models.Model):
    def __str__(self):
        return self.title

    creator = models.ForeignKey("users.User", on_delete=models.CASCADE)
    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Untitled Quiz")
    description_text = models.CharField(max_length=500)
    pub_status = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    # end_date = models.DateTimeField(
    #     'end date', default=timezone.now() + datetime.timedelta(days=1))

    def max_marks_quiz(self):
        max_marks = 0
        questions = Question.objects.filter(quiz=self)
        for question in questions:
            max_marks += question.max_marks
        return max_marks

    def was_published_recently(self):
        return self.pub_date >= timezone.now()


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
    respondant = models.ForeignKey("users.User", on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    response_time = models.DateTimeField('time taken', auto_now_add=True)
