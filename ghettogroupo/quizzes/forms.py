from django import forms
from quizzes.models import Quiz, Question, Choice


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ['title', 'description_text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder': 'Quiz title'}),
            'description_text': forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder': 'Quiz description'})
        }


class QuestionForm(forms.ModelForm):
    """docstring for QuestionForm."""

    class Meta:
        model = Question
        fields = ['question_text', 'max_marks']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder': 'Question description'}),
            'max_marks': forms.NumberInput(attrs={'class': 'form-group form-control', 'placeholder': 'Max marks'})
        }


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['choice_text', 'isAnswer']
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-group form-control', 'placeholder': 'Choice description'}),
            'isAnswer': forms.CheckboxInput()
        }


choice_set = forms.inlineformset_factory(
    Question, Choice, form=ChoiceForm, extra=1)

# choice_set = forms.formset_factory(form=ChoiceForm, extra=0)


class BaseQuestionFormset(forms.BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseQuestionFormset, self).add_fields(form, index)

        form.nested = choice_set(instance=form.instance,
                                 data=form.data if form.is_bound else None,
                                 files=form.files if form.is_bound else None,
                                 prefix='choice-%s-%s' % (
                                     form.prefix,
                                     choice_set.get_default_prefix()), extra=1)

    def is_valid(self):
        result = super(BaseChildrenFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()

        return result

    def save(self, commit=True):

        result = super(BaseChildrenFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result


question_set = forms.inlineformset_factory(
    Quiz, Question, form=QuestionForm, formset=BaseQuestionFormset, extra=1)
