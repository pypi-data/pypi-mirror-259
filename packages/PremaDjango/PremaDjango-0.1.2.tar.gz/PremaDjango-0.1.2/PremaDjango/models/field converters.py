from django.db import models


class LowercaseCharField(models.CharField):
    """Lowercases the input value."""
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value


class UppercaseCharField(models.CharField):
    """ The upper case characters of the input value. """
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            value = value.upper()
        return value


class TitleCaseCharField(models.CharField):
    """ Title cases the input value. """
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            value = value.title()
        return value


class CamelCaseCharField(models.CharField):
    """ The name of the field in camel case. """
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            value = ''.join(word.capitalize() for word in value.split())
        return value


class SnakeCaseCharField(models.CharField):
    """ snake case character field. """
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            value = '_'.join(word.lower() for word in value.split())
        return value
