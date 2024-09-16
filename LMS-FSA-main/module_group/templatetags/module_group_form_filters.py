from django import template

register = template.Library()

@register.filter(name='module_group_add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})
