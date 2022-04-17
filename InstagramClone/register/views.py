from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Account
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout as auth_logout

# Create your views here.
def register(response):
    if response.user.is_authenticated == True:
        return redirect("../../") # TODO: render main page -> Change this

    if response.method == 'POST':
        form = RegisterForm(response.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(response.POST['password'])
            user.save()
            return redirect("../../") # TODO: render main page -> Change this
        
        if len(form.errors.items()) > 0:
            form.first_error = list(form.errors.items())[0][1]
    else:
        form = RegisterForm()


    return render(response, 'register/register.html', {"form": form})

def login(response):
    if response.user.is_authenticated == True:
        return redirect("../../") # TODO: render main page -> Change this

    if response.method == 'POST':
        form = LoginForm(response.POST)
        
        if form.is_valid():
            form_log = form.cleaned_data['login']
            form_password = form.cleaned_data['password']
            filter = Account.objects.filter(email=form_log) | Account.objects.filter(username=form_log)

            if not filter: # is empty
                form.first_error = "Sua senha está incorreta."
                return render(response, 'register/login.html', {"form": form})

            user = authenticate(response, username=filter[0].username, password=form_password)

            if user is None:
                form.first_error = "Sua senha está incorreta."
                return render(response, 'register/login.html', {"form": form})

            auth_login(response, user)

            return redirect("../../") # TODO: render main page -> Change this
    else:
        form = LoginForm()

    return render(response, 'register/login.html', {"form": form})

def logout(response):
    auth_logout(response)
    return redirect('accounts/login/')
