import string

from django.core.exceptions import ValidationError


def symbol_validator(value):
    is_found = [char for char in value if not char.isalpha()]
    if is_found:
        raise ValidationError('Please avoid using symbols')