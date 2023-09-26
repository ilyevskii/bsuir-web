import re

from django.contrib.auth.models import Permission, User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator


class FullMatchRegexValidator(RegexValidator):
    def __init__(
            self, pattern, message=None, code=None, inverse_match=None, flags=None
    ):
        if not pattern.startswith('^'):
            pattern = '^' + pattern

        if not pattern.endswith('$'):
            pattern += '$'

        super().__init__(
            pattern,
            message,
            code,
            inverse_match,
            flags
        )


PHONE_PATTERN = r"\+375\s*\(\s*29\s*\)\s*(\d{3})\s*-\s*(\d{2})\s*-\s*(\d{2})"

# Check is string represent phone number in format
# +375 (29) XXX-XX-XX; using some pattern
validate_phone_number = FullMatchRegexValidator(
    PHONE_PATTERN,
    "Phone number is incorrect. Correct format is +375 (29) XXX-XX-XX.",
    code="invalid"
)


WORD_PATTERN = r"\b([A-Za-z]+)\b"
NUMBER_PATTERN = r"\b([\d\.\-]+)\b"

ADDRESS_PATTERN = fr"(({WORD_PATTERN})|({NUMBER_PATTERN})|([\s,\.\:\!]*))*"


validate_address = FullMatchRegexValidator(
    ADDRESS_PATTERN,
    "Address is incorrect. It must consist of words, numbers and codes.",
    code="invalid"
)


def get_not_negative_validator(value_name):
    return MinValueValidator(limit_value=0, message=f"{value_name} must be not negative.")


def get_positive_validator(value_name):
    return MinValueValidator(limit_value=1, message=f"{value_name} must be positive.")


def normalize_phone(phone: str):
    res = re.search(PHONE_PATTERN, phone)

    return f"+375 (29) {res.group(1)}-{res.group(2)}-{res.group(3)}"


def validate_provider(user):
    from apps.shop.models import Provider
    if not Provider.objects.filter(user_ptr_id=user.id).exists():
        raise ValidationError(f"{user.username} does not have provider permissions.")


def validate_discount(discount):
    if discount < 1 or discount > 100:
        raise ValidationError("Incorrect discount")


def is_valid(*args):
    validator = args[0]

    if len(args) == 1:
        def wrapper(*args, **kwargs) -> bool:
            try:
                validator(*args, **kwargs)
                return True
            except ValidationError:
                return False

        return wrapper

    else:
        args = args[1:]
        return is_valid(validator)(*args)
