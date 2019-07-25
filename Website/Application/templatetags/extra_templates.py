from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    if isinstance(value, str):
        value.replace(arg, '')


# the name to be used in template tag in html, the function to be applied
# register.filter(name='cut', filter_func=cut)
