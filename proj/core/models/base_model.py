
from django.db import models


class BaseModel(models.Model):

    def _assert_attribute_not_in_kwargs(self, attribute, **kwargs):
        try:
            kwargs.get(attribute)
            raise ValueError(
                f'ChessGame.{attribute} is generated by the create() method.'
            )
        except AttributeError:
            pass

    def _set_default_attribute(self, attribute, expected, **kwargs):
        try:
            field_val = kwargs.get(attribute)
            if field_val not in expected:
                expected_str = ', '.join(expected)
                raise ValueError(
                    f'ChessGame.{attribute} needs to be one of the following: '
                    f'{expected_str}.'
                )
            return kwargs
        except AttributeError:
            new_kwargs = dict(kwargs)
            new_kwargs[attribute] = expected
            return new_kwargs