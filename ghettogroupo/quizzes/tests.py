from .models import Quiz, Question, Choice, Responses
from django.test import TestCase
from users.models import User
from groups.models import Group, Membership

# Create your tests here.


class QuizCreate(TestCase):
    def __init__(self, c1, g1, title, desc):
        q = Quiz.objects.create(creator=c1, group=g1,
                                title=title, description_text=desc)


class QuizTestCase(TestCase):
    def setUp(self):
        c1 = User.objects.create(
            username='admin', email='adsa@dsf.com', fullName='Admin')
        g1 = Group.objects.create(
            name='Cooldown', type="Organization", owner=c1, description="Test Group")
        m1 = Membership(group=g1, member=c1, isOwner=True, isAssigner=True)
        QuizCreate(c1, g1, "Test Quiz 1", "Quiz Description")
        QuizCreate(c1, g1, "Test Quiz 2", "Hitchhiker's Guide")
        q1 = Quiz.objects.get(pk=1)
        q2 = Quiz.objects.get(pk=2)
        ques1 = QuestionCreate(q1.pk)
        ques2 = QuestionCreate(q2.pk)

    def test_max_marks_quiz1(self):
        quiz1 = Quiz.objects.filter(title="Test Quiz 1").first()
        self.assertEqual(quiz1.max_marks_quiz(), 6)

    def test_max_marks_quiz2(self):
        quiz2 = Quiz.objects.filter(title="Test Quiz 2").first()
        self.assertEqual(quiz2.max_marks_quiz(), 10)


class QuestionCreate(TestCase):
    def __init__(self, quiz):
        quiz1 = Quiz.objects.get(pk=quiz)
        if quiz1.title == "Test Quiz 1":
            # print("Quiz 1")
            ques1 = Question.objects.create(
                question_text="What's up?", max_marks=3, quiz=quiz1)
            ques2 = Question.objects.create(question_text="3rd letter of alphabet?",
                                            max_marks=3, quiz=quiz1)
        else:
            # print("Quiz 2")
            ques1 = Question.objects.create(
                question_text="What's the answer to every question in the universe?", max_marks=4, quiz=quiz1)
            ques2 = Question.objects.create(question_text="What's 8 x 7 ?",
                                            max_marks=6, quiz=quiz1)


class QuestionTestCase(TestCase):
    def setUp(self):
        c1 = User.objects.create(
            username='admin', email='adsa@dsf.com', fullName='Admin')
        g1 = Group.objects.create(
            name='Cooldown', type="Organization", owner=c1, description="Test Group")
        m1 = Membership(group=g1, member=c1, isOwner=True, isAssigner=True)
        QuizCreate(c1, g1, "Test Quiz 1", "Quiz Description")
        QuizCreate(c1, g1, "Test Quiz 2", "Hitchhiker's Guide")
        q1 = Quiz.objects.get(pk=1)
        q2 = Quiz.objects.get(pk=2)
        ques1 = QuestionCreate(q1.pk)
        ques2 = QuestionCreate(q2.pk)

    def test_quiz1_ques(self):
        ques1 = Question.objects.get(pk=1)
        ques2 = Question.objects.get(pk=2)
        print(Question.objects.all())

        self.assertEqual(ques1.question_text, "What's up?")
        self.assertEqual(ques2.question_text, "3rd letter of alphabet?")
        self.assertEqual(ques1.max_marks, 3)
        self.assertEqual(ques2.max_marks, 3)

    def test_quiz2_ques(self):
        print(Question.objects.all())
        ques1 = Question.objects.get(pk=3)
        ques2 = Question.objects.get(pk=4)
        self.assertEqual(ques1.question_text,
                         "What's the answer to every question in the universe?")
        self.assertEqual(ques2.question_text, "What's 8 x 7 ?")
        self.assertEqual(ques1.max_marks, 4)
        self.assertEqual(ques2.max_marks, 6)
        # choice1 =


class ChoiceCreate(TestCase):
    def __init__(self):
        ques = Question.objects.get(pk=3)
        Choice.objects.create(
            question=ques, choice_text="There is no such answer")
        Choice.objects.create(question=ques, choice_text="42", isAnswer=True)
        ques = Question.objects.get(pk=4)
        Choice.objects.create(question=ques, choice_text="42", isAnswer=True)
        Choice.objects.create(question=ques, choice_text="56")


class ChoiceTestCase(TestCase):
    def setUp(self):
        c1 = User.objects.create(
            username='admin', email='adsa@dsf.com', fullName='Admin')
        g1 = Group.objects.create(
            name='Cooldown', type="Organization", owner=c1, description="Test Group")
        m1 = Membership(group=g1, member=c1, isOwner=True, isAssigner=True)
        QuizCreate(c1, g1, "Test Quiz 1", "Quiz Description")
        QuizCreate(c1, g1, "Test Quiz 2", "Hitchhiker's Guide")
        q1 = Quiz.objects.get(pk=1)
        q2 = Quiz.objects.get(pk=2)
        QuestionCreate(q1.pk)
        QuestionCreate(q2.pk)
        ChoiceCreate()

    def test_ques1_choices(self):
        c1 = Choice.objects.get(pk=1)
        c2 = Choice.objects.get(pk=2)
        self.assertEqual(c1.choice_text, "There is no such answer")
        self.assertEqual(c2.choice_text, "42")

    def test_ques2_choices(self):
        c1 = Choice.objects.get(pk=3)
        c2 = Choice.objects.get(pk=4)
        self.assertEqual(c1.choice_text, "42")
        self.assertEqual(c2.choice_text, "56")


class ResponseCreate(TestCase):
    def __init__(self):
        c1 = Choice.objects.get(pk=2)
        c2 = Choice.objects.get(pk=4)
        User.objects.create(
            username='user1', email='user1a@dsf.com', fullName='User1')
        respondant = User.objects.get(pk=2)
        Responses.objects.create(choice=c1, respondant=respondant)
        Responses.objects.create(choice=c2, respondant=respondant)


class ResponseTestCase(TestCase):
    def setUp(self):
        c1 = User.objects.create(
            username='admin', email='adsa@dsf.com', fullName='Admin')
        g1 = Group.objects.create(
            name='Cooldown', type="Organization", owner=c1, description="Test Group")
        m1 = Membership(group=g1, member=c1, isOwner=True, isAssigner=True)
        QuizCreate(c1, g1, "Test Quiz 1", "Quiz Description")
        QuizCreate(c1, g1, "Test Quiz 2", "Hitchhiker's Guide")
        q1 = Quiz.objects.get(pk=1)
        q2 = Quiz.objects.get(pk=2)
        QuestionCreate(q1.pk)
        QuestionCreate(q2.pk)
        ChoiceCreate()
        ResponseCreate()

    def test_responses(self):
        r1 = Responses.objects.get(pk=1)
        r2 = Responses.objects.get(pk=2)
        self.assertEqual(r1.choice.choice_text, "42")
        self.assertEqual(r2.choice.choice_text, "56")

    def test_get_marks(self):
        user = User.objects.get(pk=2)
        quiz = Quiz.objects.get(pk=2)
        self.assertEqual(user.get_marks(quiz), 4)
