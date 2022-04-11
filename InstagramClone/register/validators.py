import re
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@]+\Z'
    message = _(
        'Invalid username. It may only contain letters, numbers, . and /.'
    )
    flags = re.ASCII