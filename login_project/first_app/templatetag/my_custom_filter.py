from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """

    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '')

# this is the another way to register
# register.filter('cut',cut)