from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms

from groups.models import Group
from quizzes.models import Quiz, Question, Choice
from quizzes.forms import QuizForm, QuestionForm, ChoiceForm


@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the quizzes index.")

# Create your views here.


@login_required
def quiz_page_view(request, id):
    if Membership.objects.filter(member=request.user, group__id=id):
        return HttpResponse('{} IS in group {}.\n User will be redirected to user-group-page'.format(request.user, str(code)))
    return HttpResponse('{} IS NOT in group {}.\n User will be asked to join or request to join'.format(request.user, str(code)))


@login_required
def quiz_creation_view(request, code):
    user = request.user
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.creator = user
            quiz.group = Group.objects.get(pk=code)
            quiz.save()
            # manage_questions(request, quiz)
            return redirect(reverse_lazy('add-questions', kwargs={'qid': quiz.pk}))
        # questions = question_set(request.POST, instance=quiz)
    else:
        form = QuizForm()
    return render(request, 'quizzes/create_quiz.html', {'form': form})


@login_required
def create_question_set(request, qid):
    user = request.user
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        context = {'form': form}

        # formset = choice_set(request.POST, instance=Quiz.objects.get(pk=qid))
        if form.is_valid():
            ques = form.save(commit=False)
            ques.quiz = Quiz.objects.get(pk=qid)
            ques.save()
            # create_choice_set(request, question=ques.pk)
            return redirect(reverse_lazy('add-choices', kwargs={'question': ques.pk}))
            # manage_questions(request, quiz)
            return render(request, 'quiz-home')
        # questions = question_set(request.POST, instance=quiz)
    else:
        form = QuestionForm()
        # formset = choice_set(request.POST)
        context = {'form': form}
    return render(request, 'quizzes/add_questions.html', context)


@login_required
def create_choice_set(request, question):
    user = request.user
    choice_set = forms.inlineformset_factory(
        Question, Choice, form=ChoiceForm, extra=1)
    formset = choice_set(instance=Question.objects.get(pk=question))
    context = {'formset': formset}

    if request.method == 'POST':
        # form = QuestionForm(request.POST)
        formset = choice_set(
            request.POST, instance=Question.objects.get(pk=question))
        # for choice in formset.forms:
        #     print(choice)
        if formset.is_valid():
            formset.save()
            # return redirect('parent_view', parent_id=parent.id)
            # manage_questions(request, quiz)
            return render(request, 'quiz-home')
        # questions = question_set(request.POST, instance=quiz)
    else:
        # form = QuestionForm()
        # formset = choice_set(request.POST)
        context = {'formset': formset}
    return render(request, 'quizzes/add_questions.html', context)


@login_required
def test_print(request):
    quiz = Quiz.objects.all()
    context = {'quizzes': quiz}
    return render(request, 'quizzes/manage_questions.html', context)
