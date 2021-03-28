from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import CustomUser

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'phone', 'email', 'password1', 'password2',)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('email') is None and cleaned_data.get('phone') is None:
            raise ValidationError('Please Enter an Email or a Phone number')
        return cleaned_data


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'phone', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username/phone')


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'bio', 'website', 'avatar')
