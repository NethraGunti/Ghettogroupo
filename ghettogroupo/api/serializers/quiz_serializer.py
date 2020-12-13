from rest_framework import serializers

from quizzes.models import Quiz, Question, Choice


class CreateChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        exclude = ['question']

#
# class EditChoiceSerializer(serializers.ModelSerializer)
#     class Met


class CreateQuestionSerializer(serializers.ModelSerializer):
    choices = CreateChoiceSerializer(many=True)

    class Meta:
        model = Question
        exclude = ['quiz']
        include = ['choices']


class CreateQuizSerializer(serializers.ModelSerializer):
    questions = CreateQuestionSerializer(many=True)

    class Meta:
        model = Quiz
        exclude = ['creator', 'pub_date']
        include = ['questions']

    def save(self, user, **kwargs):
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        print(validated_data)
        self.instance = self.create(user, validated_data)
        self.instance.save()
        return self.instance

    def create(self, user,  validated_data):
        # print("tuturu")
        questions = validated_data['questions']
        description_text = validated_data['description_text']
        title = validated_data['title']
        group_code = validated_data['group']
        quiz = Quiz.objects.create(
            creator=user, title=title, description_text=description_text, group=group_code)
        quiz.save()

        for question in questions:
            q_text = question['question_text']
            max_marks = question['max_marks']
            choices = question['choices']
            ques = Question.objects.create(
                quiz=quiz, question_text=q_text, max_marks=max_marks)
            ques.save()

            for choice in choices:
                c_text = choice['choice_text']
                isAnswer = choice['isAnswer']
                choc = Choice.objects.create(
                    question=ques, choice_text=c_text, isAnswer=isAnswer)
                choc.save()
        return quiz


class UpdateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        exclude = ['creator', 'pub_date', 'end_date']
