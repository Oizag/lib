from django import template

register = template.Library()


@register.filter(name="add_form_class")
def add_form_class(value, arg):
    """
    {{ form.subject|class:'MyClass' }}
    """
    return value.as_widget(attrs={"class": arg})
