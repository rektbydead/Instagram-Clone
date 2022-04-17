from django.shortcuts import render
from register.models import Account

# Create your views here.
def default(response):
    pass

def inbox(response):
    pass

def profile(response, username):
    filter = Account.objects.filter(username=username)

    if not filter:
        return render(response, 'main/user_does_not_exists.html')

    return render(response, 'main/user_exists.html', { "user": filter[0]})