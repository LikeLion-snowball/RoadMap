from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, username, email, phonenum, major, address, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             username=username,
#             email=email,
#             phonenum=phonenum,
#             major=major,
#             address=address,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, phonenum, major, address, password):
#         user = self.create_user(
#             username=username,
#             email=email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

class CustomUser(AbstractUser):
    email = models.EmailField()
    phonenum = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    portfolio_isPrivate = models.BooleanField(default=True)

    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)

    # objects = UserManager()

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True

    # @property
    # def is_staff(self):
    #     return self.is_admin