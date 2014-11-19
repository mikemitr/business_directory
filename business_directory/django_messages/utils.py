import django
from django_messages.utils import get_user_model


def get_username_field():
    if django.VERSION[:2] >= (1, 5):
        return get_user_model().email
    else:
        return 'email'