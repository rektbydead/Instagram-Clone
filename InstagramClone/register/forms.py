from django import forms
from register.models import Account
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        label = "",
        widget = forms.EmailInput(
            attrs = {
                'placeholder': 'Email', 
                'autofocus': True
            },
        ),
        error_messages = None,
        required = True,
    )

    profile_name = forms.CharField(
        max_length = 32, 
        label = "", 
        widget = forms.TextInput(attrs = {'placeholder': 'Profile Name'}),
        required = True,
        strip = True,
    )

    username = forms.CharField( #Add regex to block space, not letter, underline(_) or periods (.)
        max_length = 16, 
        label = "",
        widget = forms.TextInput(attrs = {'placeholder': 'Username'}),
        required = True,
        strip = True,
    )

    password = forms.CharField(
        max_length = 32, 
        strip = False,
        label = "",
        widget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password'}),
        required = True,
    )

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


    class Meta:
        model = Account
        fields = ["email", "username", "profile_name", "password"]


