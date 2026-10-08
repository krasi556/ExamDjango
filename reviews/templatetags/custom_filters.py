from django import template

register = template.Library()


@register.filter
def amount_stars(rating):
    if not rating:
        return ''
    number = round(rating)
    outcome = '⭐' * number + '☆' * (5 - number)
    return outcome


@register.filter
def reviews_count(objects):
    amount = sum(1 for el in objects)
    return amount