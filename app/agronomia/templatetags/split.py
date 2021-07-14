from django import template

register = template.Library()

@register.filter
def split(arg):
    v =arg.replace("_"," ")
    return v.replace("/"," ").capitalize()
