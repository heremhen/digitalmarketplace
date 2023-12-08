from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import UserProfile


class CreateUserForm(UserCreationForm):  # Registration form
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "email",
                }
            ),
            "password1": PasswordInput(),
            "password2": PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is invalid")

        if len(email) >= 350:
            raise forms.ValidationError("Your email is too long")

        return email


class LoginForm(AuthenticationForm):  # Login form
    username = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "input input-bordered w-full max-w-xs",
                "type": "text",
                "placeholder": "username",
            }
        )
    )
    password = forms.CharField(widget=PasswordInput())


class UpdateUserForm(forms.ModelForm):  # Update form
    password = None

    class Meta:
        model = User
        fields = ["username", "email"]
        exclude = ["password1", "password1"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "email",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is invalid")

        if len(email) >= 350:
            raise forms.ValidationError("Your email is too long")

        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]
