from django.db import models
from register.models import Account

# Create your models here.
class Publication(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True, blank=False)
    description = models.TextField(max_length=300, blank=True, null=False)
    photo = models.ImageField(null=False, blank=False)


class Story(Publication):
    pass


