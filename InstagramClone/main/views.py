from django.shortcuts import render, redirect
from register.models import Account

# Create your views here.
def default(response):
    if response.user.is_authenticated == False:
        return redirect('accounts/login/')

    return render(response, 'main/home.html')

def inbox(response):
    pass

def profile(response, username):
    filter = Account.objects.filter(username=username)

    if not filter:
        return render(response, 'main/user_does_not_exists.html')

    return render(response, 'main/user_exists.html', { "user": filter[0]})