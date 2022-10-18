from email.policy import default
from django.db import models

# Create your models here.

class Question(models.Model):
    # savol oddiy matnli maydon
    question = models.TextField()
    # javoblar char, belgilar qabul qluvchi maydon
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    # togri javob raqami raqamli musbat son
    right_answer = models.PositiveIntegerField(default=0)    

    # savol obyektiga murojat vaqti savol matni qaytaradi
    def __str__(self):
        return str(self.question)