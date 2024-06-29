from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    topic_text = models.CharField(max_length=250)

    def __str__(self):
        return self.topic_text


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question_text[:50]


class Choice(models.Model):
    choice_text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text[:50]

