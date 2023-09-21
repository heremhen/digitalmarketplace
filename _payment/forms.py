from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            "full_name",
            "email",
            "address1",
            "address2",
            "city",
            "state",
            "zipcode",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "Full name*",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "Email address*",
                }
            ),
            "address1": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "Address 1*",
                }
            ),
            "address2": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "Address 2*",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "City*",
                }
            ),
            "state": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "State (Optional)",
                }
            ),
            "zipcode": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full max-w-xs",
                    "type": "text",
                    "placeholder": "Zip code (Optional)",
                }
            ),
        }
        exclude = [
            "user",
        ]