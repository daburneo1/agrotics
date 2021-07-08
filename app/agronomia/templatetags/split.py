from django import template

register = template.Library()

def hola(value): # Only one argument.
    """Converts a string into all lowercase"""
    print(value)
    return value.lower()