from django.db import models

# Create your models here.
import datetime

from django.utils import timezone
from django.db import models


class Question(models.Model):#two fields: question text and public date
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):#choice text and votes
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#foreignKey is choice related to a single question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text