import random

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def color_by_hourly_rate(rate):
    if rate > 100:
        return mark_safe(f"<span>Too expensive just get AI instead </span>")
    elif rate > 80:
        color = '#DC3545'
    elif rate > 70:
        color = '#ED5A2D'
    elif rate > 60:
        color = '#FEA00E'
    elif rate > 20:
        color = '#FFC107'
    else:
        color = '#198754'
    return mark_safe(f'<span style="color: {color}">{rate}</span>')


ratings = {
    1: "Works on my machine, nowhere else",
    2: "Copy-pasted from Stack Overflow",
    3: "Almost as good as AI",
    4: "Suspiciously good, is it AI?",
    5: "Better than AI (don't tell the AI)",
}


@register.filter
def stars_cont(value):
    if value is not None and not isinstance(value, str):
        rounded_number = round(value)
        number = max(1, min(5, rounded_number))
        return ratings[number]
    return 'No rating yet, probably because he is busy fixing your code'
