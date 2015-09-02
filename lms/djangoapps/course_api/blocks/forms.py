"""

"""
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, Field, MultipleHiddenInput


class ListField(Field):
    """
    Field for a list of strings
    """
    widget = MultipleHiddenInput


class BlockListGetForm(Form):
    """
    A form to validate query parameters in the block list retrieval endpoint
    """
    user = CharField(required=True) # TODO return all blocks if user is not specified by requesting staff user
    fields = ListField(required=False, initial='graded,format,student_view_data,student_view_multi_device')
    student_view_data = ListField(required=False)
    block_counts = ListField(required=False)
    depth = CharField(required=False, initial='0')

    def clean_fields(self):
        # always include type and display_name fields
        self.cleaned_data['fields'] = set(self.cleaned_data['fields']) | {'type', 'display_name'}

    def clean_depth(self):
        value = self.cleaned_data['depth']
        if value == "all":
            return None
        try:
            return int(value)
        except ValueError:
            raise ValidationError("'{}' is not a valid depth value".format(value))

    def clean_user(self):
        username = self.cleaned_data['user']
        if username.lower() != self.initial['request'].user.username.lower():
            # verify user is staff and get requested user object
            raise NotImplementedError
