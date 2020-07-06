from django.db import models


# Create your models here.
class Question(models.Model):
    body = models.CharField(max_length=250)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish']


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)