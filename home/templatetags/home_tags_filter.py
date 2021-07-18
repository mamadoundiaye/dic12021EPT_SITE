from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='tronquer')
def tronquer(value):
    pass


@register.filter(name='tronquer')
@stringfilter # même si chaine n'est pas de type str, elle sera convertit en str
def filter_upper(chaine: str):
    pass