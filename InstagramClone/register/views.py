from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Account
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LogoutView

# Create your views here.
def register(response):
    if response.user.is_authenticated == True:
        pass # TODO: Render main instagram page

    if response.method == 'POST':
        form = RegisterForm(response.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(response.POST['password'])
            user.save()
            pass # TODO: Render main instagram page
        
        if len(form.errors.items()) > 0:
            form.first_error = list(form.errors.items())[0][1]
    else:
        form = RegisterForm()


    return render(response, 'register/register.html', {"form": form})

def login(response):
    if response.user.is_authenticated == True:
        return redirect("https://google.com/") # TODO: Render main instagram page

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

            return redirect("https://google.com/")
            ##pass # TODO: Render main instagram page
    else:
        form = LoginForm()

    return render(response, 'register/login.html', {"form": form})

#def logout(response):
#    LogoutView()
