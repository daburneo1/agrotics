from django import template

register = template.Library()


@register.filter
def split(arg):
    v = arg.replace("_", " ")
    v = v.replace("<int:pk>", "")
    v= v.replace("edit", "Editar")
    return v.replace("/", " ").capitalize()
