from django.db import models
from category.models import Category
from subject.models import Subject

class Question(models.Model):
    #subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name