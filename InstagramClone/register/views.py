from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.user.is_authenticated == True:
        pass # TODO: Render main instagram page

    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
            pass # TODO: Render main instagram page

    else:
        form = RegisterForm()
    
    return render(response, 'register/register.html', {"form": form})