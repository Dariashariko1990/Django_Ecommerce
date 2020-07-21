from users.models import User
from django.core.validators import EmailValidator
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwars):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                print(user)
                return user

        return None

