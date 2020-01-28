from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django import forms
from django.core.exceptions import ObjectDoesNotExist
import isodate

# Create your models here.
class modules(models.Model):
    module_name = models.CharField(max_length = 200)

class questions(models.Model):
    questions_under = models.ForeignKey(modules, on_delete=models.SET_NULL,null=True)
    question_name = models.CharField(max_length = 200)

class answers(models.Model):
    answers_under = models.ForeignKey(questions, on_delete=models.SET_NULL,null=True)
    first_choice = models.CharField(max_length = 200)
    second_choice = models.CharField(max_length = 200)
    third_choice = models.CharField(max_length = 200)
    fourth_choice = models.CharField(max_length = 200)
    correct_answer = models.CharField(max_length = 200, null=True)

class scores(models.Model):
    gameId = models.CharField(max_length = 100, null=True)
    scores = models.IntegerField(null=True)