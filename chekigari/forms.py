from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = 'Enter username'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter username'
        })

        # self.fields['email'].label = 'Enter email'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter email'
        })

        # self.fields['password1'].label = 'Enter password'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter password'
        })

        # self.fields['password2'].label = 'Repeat password'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Repeat password'
        })

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']




class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = 'Enter username'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter username'
        })


        # self.fields['password1'].label = 'Enter password'
        self.fields['password'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter password'
        })

    class Meta:
        model = User
        fields = ['username', 'password']
