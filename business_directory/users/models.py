# -*- coding: utf-8 -*-
# Import the AbstractUser model
from authtools.models import AbstractEmailUser


# Subclass AbstractUser
class User(AbstractEmailUser):
    pass
    # def __unicode__(self):
    #     return self.username