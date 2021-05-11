from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class UserModel(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
