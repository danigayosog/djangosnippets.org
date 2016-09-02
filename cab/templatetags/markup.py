import bleach
from django import template
from django.utils.safestring import mark_safe
from markdown import markdown as markdown_func

register = template.Library()


@register.filter
def markdown(value):
    """
    Run Markdown over a given value.
    """
    return mark_safe(markdown_func(value))


@register.filter
def safe_markdown(value):
    """
    Strip raw HTML and run Markdown over a given value.
    """
    return mark_safe(bleach.clean(markdown_func(value)))
