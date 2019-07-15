from django.db import models


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.question.text

    class Meta:
        order_with_respect_to = 'question'
