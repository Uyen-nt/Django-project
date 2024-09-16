# question_bank/templatetags/form_filters.py

from django import template

register = template.Library()

@register.filter(name='add_question_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})