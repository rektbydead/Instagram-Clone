from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publication():
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True, blank=False)
    description = models.TextField(max_length=300, blank=True, null=False)

class Story(Publication):
    pass


