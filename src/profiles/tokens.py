from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from .models import CustomUser


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(CustomUser.email_confirmed)
        )


account_activation_token = AccountActivationTokenGenerator()
