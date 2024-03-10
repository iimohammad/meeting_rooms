from django import template

register = template.Library()

@register.simple_tag
def get_url(model, status):
    
    return model.get_absolute_url(status)