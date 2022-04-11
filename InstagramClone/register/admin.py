from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.

admin.site.register(Account)
#admin.site.register(Follower)