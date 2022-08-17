import datetime

from django.core.validators import MaxValueValidator, RegexValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


SLUG_REGEX = RegexValidator(r'^[\w-]+$')
