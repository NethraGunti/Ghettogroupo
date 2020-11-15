from nested_inline.admin import NestedStackedInline, NestedModelAdmin 

from django.contrib import admin

from quizzes.models import Quiz, Question, Choice, Responses

class ChoicesInline(NestedStackedInline):
    model = Choice
    extra = 1

class QuestionInline(NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoicesInline]

class QuizAdmin(NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Responses)
