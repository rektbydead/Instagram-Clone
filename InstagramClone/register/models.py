from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from .validators import UsernameValidator
import json
from django.contrib.auth.models import PermissionsMixin

class AccountManager(BaseUserManager):
    def create_user(self, username, email, profile_name, password=None):
        #if not username:
        #    raise ValueError('Username does not exist')

        #if not email:
        #    raise ValueError('Email does not exist')

        #if not profile_name:
        #    raise ValueError('Profile name does not exist')      

        user = self.model(
            username = username.lower(),
            email = email.lower(),
            profile_name = profile_name,
        )

        #password2 = make_password(password)

        #print(password + " -> " + password2)
        user.set_password(password) #make_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, profile_name, password):
        user = self.create_user(
            username = username.lower(),
            email = email.lower(),
            profile_name = profile_name,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Account(AbstractBaseUser, PermissionsMixin):
    #User Fields
    email = models.EmailField(unique=True, max_length=254, blank=False,
        error_messages={
            'unique': _("An account with that email already exists."),
        }
    )
    username = models.CharField(unique=True, max_length=32, blank=False, 
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        validators=[UsernameValidator],
    )
    profile_name = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=120, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='./profile_photos/', default='default_profile_photo.jpg')

    #Mandatory Fields
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #Fields used to login
    USERNAME_FIELD = 'username'
    #EMAIL_FIELD = 'email'

    #Required fields
    REQUIRED_FIELD = ['email', 'profile_name']

    #Set Manager
    objects = AccountManager()

    #What to print 
    def __str__(self):
        return json.dumps({
            'email': self.email,
            'username': self.username,
            'profile_name': self.profile_name,
            'description': self.description,
            'date_of_birth': self.date_of_birth,
            'password': self.password,
        })

    #Users permission (doesn't matter but it's mandatory)
    def has_perm(self, perm, obj=None):
        return self.is_admin

    #Related to permission
    def has_module_perms(self, app_label):
        return True

class Follower():
    user_being_followed = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    follower = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
