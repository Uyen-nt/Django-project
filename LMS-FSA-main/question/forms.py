from django import forms
from .models import Question, Answer, Category, Subject  
from django.forms import modelformset_factory, inlineformset_factory

# Form for creating and editing questions
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'category', 'question_text']

    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

# Form for creating and editing answers
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']

# Formset for handling multiple answers per question
AnswerFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, extra=1)

# Formset for handling multiple questions
QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=1)
