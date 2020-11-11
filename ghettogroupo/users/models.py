from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from groups.models import Groups


INTERESTS = [
    ("Agriculture", "Agriculture"),
    ("Arts and Entertainment", "Arts and Entertainment"),
    ("Education", "Education"),
    ("Food", "Food"),
    ("Hardware and Automobiles", "Hardware and Automobiles"),
    ("Healthcare and Medicine", "Healthcare and Medicine"),
    ("Law and Enforcement", "Law and Enforcement"),
    ("Sales and Management", "Sales and Management"),
    ("Science and Technology", "Science and Technology"),
]

OCCUPATIONS = [
    ("Actor", "Actor"),
    ("Architecture", "Architecture"),
    ("Armed Forces", "Armed Forces"),
    ("Artisan", "Artisan"),
    ("Automobile", "Automobile"),
    ("Construction", "Construction"),
    ("Dancer", "Dancer"),
    ("Design and Creativity", "Design and Creativity"),
    ("Education", "Education"),
    ("Engineering", "Engineering"),
    ("Farming", "Farming"),
    ("Finance", "Finance"),
    ("Fine Arts", "Fine Arts"),
    ("Food and Services", "Food and Services"),
    ("Human Resources", "Human Resources"),
    ("Information Technology", "Information Technology"),
    ("Judiciary", "Judiciary"),
    ("Legislation ", "Legislation "),
    ("Marketing", "Marketing"),
    ("Medical", "Medical"),
    ("Medical practitioner", "Medical practitioner"),
    ("Musician", "Musician"),
    ("Nursing Staff", "Nursing Staff"),
    ("Pharmacist", "Pharmacist"),
    ("Producer", "Producer"),
    ("Public health executive", "Public health executive"),
    ("Researcher", "Researcher"),
    ("Sales", "Sales"),
    ("Social Sciences", "Social Sciences"),
    ("Water supply", "Water supply"),
    ("Wood and metalwork", "Wood and metalwork"),
    ("Writer", "Writer")
]


class User(AbstractUser):
    email = models.EmailField(_('Email Address'), unique=True)
    username = models.CharField(max_length=20, unique=True)
    firstName = models.CharField(_("First Name"), max_length=20)
    lastName = models.CharField(_("Last Name"), max_length=20, blank=True, null=True)
    USERNAME = 'username'
    REQUIRED_FIELDS = ['email', 'firstName']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
    
    @property
    def profile(self):
        return UserProfile.objects.get(user=self)

    @property
    def interests(self):
        return Interest.objects.filter(user=self)

    # def inGroup(self, group):
        # return True if 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(_("Age"))
    organization = models.CharField(_("Organization"), max_length=75, help_text="write full form of the organization")
    occupation = models.CharField(_("Occupation"), choices=OCCUPATIONS, max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.CharField(_("Interest"), max_length=100, choices=INTERESTS)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'