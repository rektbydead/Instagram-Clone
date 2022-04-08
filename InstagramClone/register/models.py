from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(User):
    description = models.CharField(max_length=300)

class Follower():
    user_being_followed = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    follower = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
